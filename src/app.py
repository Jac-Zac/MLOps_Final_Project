import streamlit as st

from db import (get_poster_url, get_random_films, load_data_and_index,
                load_embedding_model)
from movie_utils import MovieDisplay, MovieSearch, SidebarFilters, setup_page


@st.cache_resource
def get_cached_data():
    """Load and cache the data and index"""
    api_key = st.secrets["tmdb"]["api_key"]
    return load_data_and_index(api_key)


def main():
    setup_page()
    model = load_embedding_model()
    df, index = get_cached_data()

    if df is None or index is None:
        st.error("Failed to load movie data. Please try again later.")
        return

    movie_search = MovieSearch(model, index, df)
    min_rating, num_films = SidebarFilters.render()
    filtered_df = df[df["vote_average"].astype(float) >= min_rating]

    if "show_featured" not in st.session_state:
        st.session_state.show_featured = True

    query = st.text_input("🔍 Search for a movie:")
    if query:
        similar_movies = movie_search.search_movies(query, num_films, min_rating)
        if similar_movies:
            st.markdown("## 🎥 Search Results")
            MovieDisplay.display_movie_grid(similar_movies, get_poster_url)
        else:
            st.warning("No movies found matching your criteria.")
        st.session_state.show_featured = False

    st.markdown("## 🎲 Discover Random Films")
    if st.button("🎲 Get Random Films"):
        if filtered_df.empty:
            st.error("No movies found with selected rating")
        else:
            random_films = get_random_films(filtered_df, num_films)
            MovieDisplay.display_movie_grid(random_films, get_poster_url)
            st.session_state.show_featured = False

    if st.session_state.show_featured:
        st.markdown("## 🎥 Featured Movies")
        showcase_films = get_random_films(df, 5)
        MovieDisplay.display_movie_grid(showcase_films, get_poster_url)


if __name__ == "__main__":
    main()
