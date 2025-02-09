import pandas as pd
import requests
import streamlit as st


@st.cache_data
def load_data():
    """Loads the movie dataset from local CSV"""
    try:
        return pd.read_csv("data/films.csv")
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


def get_random_films(df, num_films):
    """Return a list of random films from the dataframe."""
    return df.sample(min(num_films, len(df))).to_dict(orient="records")


def get_poster_url(title, year):
    """Fetches movie poster URL from TMDb API using Streamlit Secrets"""
    try:
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": st.secrets["tmdb"]["api_key"],
                "query": title,
                "year": year,
                "include_adult": False,
            },
        )
        results = response.json().get("results", [])
        if results and results[0].get("poster_path"):
            return f"https://image.tmdb.org/t/p/w780{results[0]['poster_path']}"
    except Exception as e:
        st.error(f"Poster fetch error: {e}")
    return None
