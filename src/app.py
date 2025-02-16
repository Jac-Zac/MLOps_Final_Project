# app.py

import streamlit as st
import torch
from sentence_transformers import SentenceTransformer

from db import get_poster_url, get_random_films, load_data_and_index
from movie_utils import MovieDisplay, MovieSearch, SidebarFilters, setup_page


def initialize_model():
    """Initialize the sentence transformer model with error handling"""
    try:
        # Suppress the torch.classes warning
        import warnings

        warnings.filterwarnings("ignore", category=UserWarning, module="torch.classes")

        return SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as e:
        st.error(f"Error initializing model: {str(e)}")
        st.stop()


def main():
    # Setup and configuration
    setup_page()

    # Load model and data
    model = initialize_model()
    api_key = st.secrets["tmdb"]["api_key"]
    df, index = load_data_and_index(api_key)

    # Initialize components
    movie_search = MovieSearch(model, index, df)

    # Get filters from sidebar
    min_rating, num_films = SidebarFilters.render()
    filtered_df = df[df["vote_average"].astype(float) >= min_rating]

    # Initialize state for tracking if we should show featured movies
    if "show_featured" not in st.session_state:
        st.session_state.show_featured = True

    # Search functionality
    query = st.text_input("🔍 Search for a movie:")
    if query:
        similar_movies = movie_search.search_movies(query, num_films, min_rating)
        if similar_movies:
            st.markdown("## 🎥 Search Results")
            MovieDisplay.display_movie_grid(similar_movies, get_poster_url)
        else:
            st.warning("No movies found matching your criteria.")
        st.session_state.show_featured = False

    # Random film selection
    st.markdown("## 🎲 Discover Random Films")
    if st.button("🎲 Get Random Films"):
        if filtered_df.empty:
            st.error("No movies found with selected rating")
        else:
            random_films = get_random_films(filtered_df, num_films)
            MovieDisplay.display_movie_grid(random_films, get_poster_url)
            st.session_state.show_featured = False

    # Featured movies (shown only when not searching and random films haven't been requested)
    if st.session_state.show_featured:
        st.markdown("## 🎥 Featured Movies")
        showcase_films = get_random_films(df, 5)
        MovieDisplay.display_movie_grid(showcase_films, get_poster_url)


if __name__ == "__main__":
    main()
