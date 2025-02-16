import csv
import os

import faiss
import numpy as np
import pandas as pd
import requests
import streamlit as st
from sentence_transformers import SentenceTransformer


def fetch_movies(api_key, output_csv, max_pages=500):
    all_movies = []

    for page in range(1, max_pages + 1):
        params = {
            "api_key": api_key,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1000,
            "page": page,
        }
        response = requests.get(
            "https://api.themoviedb.org/3/discover/movie", params=params
        )
        data = response.json()

        if "results" in data:
            all_movies.extend(data["results"])
        else:
            break

    print(f"Total movies fetched: {len(all_movies)}")

    fields = [
        "genre_ids",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "vote_average",
        "title",
    ]

    with open(output_csv, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for movie in all_movies:
            row = {field: movie.get(field, "") for field in fields}
            writer.writerow(row)

    print(f"CSV file '{output_csv}' has been created.")


def create_vector_database(input_csv, output_index):
    """
    Creates a Faiss index from the 'overview' column of a CSV file using SentenceTransformer embeddings.
    """
    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{input_csv}'")
        return False  # Indicate failure
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False

    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(
            df["overview"].fillna("").tolist(), convert_to_numpy=True
        )

        embedding_dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(embedding_dimension)
        index.add(embeddings)

        faiss.write_index(index, output_index)
        print(f"FAISS index saved to '{output_index}'")
        return True  # Indicate success
    except Exception as e:
        print(f"Error creating index: {e}")
        return False


def load_data_and_index(api_key):
    """
    Loads the movie dataset from a local CSV file, downloads it if not present,
    and loads the corresponding Faiss index.  If the index is not present, it creates it.
    """
    csv_path = "data/movies.csv"
    index_path = "data/movies.index"

    # Data Loading
    if not os.path.exists(csv_path):
        st.warning("Data file not found. Fetching data...")
        # Ensure fetch_movies is correctly defined and accessible
        if not fetch_movies(api_key, csv_path):  # Call the function to fetch data
            st.error("Failed to fetch data.")
            return None, None

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None  # Return None for both data and index

    # Index Loading/Creation
    if not os.path.exists(index_path):
        st.warning(f"Index file not found at {index_path}. Creating it now...")
        if not create_vector_database(csv_path, index_path):
            st.error("Failed to create Faiss index.")
            return df, None  # Return dataframe but no index
    try:
        index = faiss.read_index(index_path)
        print(f"Successfully loaded index from: {index_path}")
    except Exception as e:
        st.error(f"Error loading index: {e}")
        return df, None  # Return the dataframe, but None for the index

    return df, index


def get_random_films(df, num_films):
    """Return a list of random films from the dataframe."""
    return df.sample(min(num_films, len(df))).to_dict(orient="records")


def search_similar_movies(query, df, num_films=5):
    """Search for similar movies based on the query."""
    query_embedding = model.encode(query).astype(np.float32)
    _, similar_movie_indices = index.search(np.array([query_embedding]), num_films)
    return df.iloc[similar_movie_indices[0]].to_dict(orient="records")


def get_poster_url(title):
    """Fetches movie poster URL from TMDb API using Streamlit Secrets"""
    try:
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": st.secrets["tmdb"]["api_key"],
                "query": title,
                "include_adult": False,
            },
        )
        results = response.json().get("results", [])
        if results and results[0].get("poster_path"):
            return f"https://image.tmdb.org/t/p/w780{results[0]['poster_path']}"
    except Exception as e:
        st.error(f"Poster fetch error: {e}")
    return None
