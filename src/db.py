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


def get_random_film(df):
    """Returns a random movie from the dataset"""
    return df.sample(1).iloc[0] if not df.empty else None


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
