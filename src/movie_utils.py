# movie_utils.py

from itertools import islice
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import streamlit as st


class MovieDisplay:
    """Component for displaying movie information"""

    @staticmethod
    def display_movie_card(col, film: Dict, poster_url: Optional[str]) -> None:
        """Display a single movie card in a column."""
        with col:
            if poster_url:
                st.image(poster_url, use_container_width=True)
            else:
                st.warning("Poster not available")

            # Title container with fixed height to ensure uniform spacing
            st.markdown(
                f"""
                <div style="
                    height: 4em; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center;
                    overflow: hidden;
                    text-align: center;
                ">
                    <span style="font-size: 1.5em; color: #FFFFFF;">🎞️ {film['original_title']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Info container styled for dark theme
            st.markdown(
                f"""
                <div style="
                    display: flex; 
                    justify-content: space-around; 
                    align-items: center;
                    padding: 0.5em; 
                    border-radius: 10px; 
                    background-color: #333333;
                    color: #FFFFFF;
                    font-weight: bold;
                    margin-top: 0.5em;
                ">
                    <div>📅 {film['release_date']}</div>
                    <div>⭐ {film['vote_average']:.1f}</div>
                    <div>🌍 {film['original_language']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    @staticmethod
    def display_movie_grid(movies: List[Dict], get_poster_url_func) -> None:
        """Display a grid of movie cards with a max of 5 per row."""
        if not movies:
            st.warning("No movies found matching your criteria.")
            return

        # Process movies in chunks of 5
        def chunked(iterable, size):
            it = iter(iterable)
            return iter(lambda: list(islice(it, size)), [])

        for movie_chunk in chunked(movies, 5):
            cols = st.columns(len(movie_chunk))  # Create only needed columns
            for col, film in zip(cols, movie_chunk):
                poster_url = get_poster_url_func(film["original_title"])
                MovieDisplay.display_movie_card(col, film, poster_url)

            st.markdown("---")  # Add a separator between rows


class MovieSearch:
    """Handles movie search functionality"""

    def __init__(self, model, index, df: pd.DataFrame):
        self.model = model
        self.index = index
        self.df = df

    def search_movies(
        self, query: str, num_films: int, min_rating: float
    ) -> List[Dict]:
        """
        Search for movies similar to the query that meet the minimum rating requirement

        Args:
            query: Search query string
            num_films: Number of films to return
            min_rating: Minimum rating threshold

        Returns:
            List of filtered similar movies
        """
        # Get more results than needed to account for filtering
        search_multiplier = 3  # Get 3x more results initially to allow for filtering
        initial_num_films = num_films * search_multiplier

        query_embedding = self.model.encode(query).astype(np.float32)
        _, similar_movie_indices = self.index.search(
            np.array([query_embedding]), initial_num_films
        )

        # Get all similar movies
        similar_movies = self.df.iloc[similar_movie_indices[0]]

        # Filter by rating and convert to list of dicts
        filtered_movies = (
            similar_movies[similar_movies["vote_average"].astype(float) >= min_rating]
            .head(num_films)
            .to_dict(orient="records")
        )

        return filtered_movies


class SidebarFilters:
    """Handles sidebar filter components"""

    @staticmethod
    def render() -> Tuple[float, int]:
        """Render sidebar filters and return selected values"""
        with st.sidebar:
            st.markdown("## 🔍 Filter Movies")
            min_rating = st.slider("Minimum Rating", 0.0, 10.0, 5.0, 0.1)
            num_films = st.slider("Number of Films", 1, 10, 3, key="num_films")
        return min_rating, num_films


def setup_page():
    """Configure the Streamlit page"""
    st.set_page_config(page_title="PickaFilm", page_icon="🎬", layout="wide")
    st.markdown(
        """
    # 🎬 PickaFilm
    Discover your next favorite movie!
    """
    )
