# movie_utils.py

from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import streamlit as st


class MovieDisplay:
    """Component for displaying movie information"""

    @staticmethod
    def display_movie_card(col, film: Dict, poster_url: Optional[str]) -> None:
        """Display a single movie card in a column"""
        with col:
            if poster_url:
                st.image(poster_url, use_container_width=True)
            else:
                st.warning("Poster not available")
            st.markdown(f"**🎞️ {film['original_title']}**")
            st.markdown(f"⭐ {film['vote_average']}")

    @staticmethod
    def display_movie_grid(movies: List[Dict], get_poster_url_func) -> None:
        """Display a grid of movie cards"""
        if not movies:
            st.warning("No movies found matching your criteria.")
            return

        cols = st.columns(len(movies))
        for col, film in zip(cols, movies):
            poster_url = get_poster_url_func(film["original_title"])
            MovieDisplay.display_movie_card(col, film, poster_url)
        st.markdown("---")


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
