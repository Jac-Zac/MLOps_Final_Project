# main.py
import streamlit as st

from db import get_poster_url, get_random_film, load_data

# App configuration
st.set_page_config(page_title="PickaFilm", page_icon="🎬", layout="wide")

# Load data
df = load_data()

# UI elements
st.markdown(
    """
# 🎬 PickaFilm
Discover your next favorite movie!
"""
)

with st.sidebar:
    st.markdown("## 🔍 Filter Movies")
    min_rating = st.slider("Minimum Rating", 0.0, 10.0, 7.0, 0.1)
    filtered_df = df[df["Movie Rating"].astype(float) >= min_rating]

if st.button("🎥 Pick Random Film"):
    if filtered_df.empty:
        st.error("No movies found with selected rating")
    else:
        film = get_random_film(filtered_df)
        poster_url = get_poster_url(film["Movie Name"], film["Year of Release"])

        # Create columns layout
        col1, col2 = st.columns([1, 2])

        with col1:
            if poster_url:
                st.image(poster_url, use_container_width=True)
            else:
                st.warning("Poster not available")

        with col2:
            st.markdown(
                f"""
            ## 🎞️ {film['Movie Name']}
            **📅 Year:** {film['Year of Release']}  
            **⏱ Duration:** {film['Watch Time']}  
            **⭐ Rating:** {film['Movie Rating']}  
            **🏆 Meatscore:** {film['Meatscore of movie']}  
            **🗳 Votes:** {film['Votes']}  
            **💰 Gross:** {film['Gross']}

            **📖 Description:**  
            {film['Description']}
            """
            )

        st.markdown("---")
