import streamlit as st

from db import get_poster_url, get_random_films, load_data

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
    num_films = st.slider("Number of Films", 1, 10, 3)  # Slider for number of films
    filtered_df = df[df["Movie Rating"].astype(float) >= min_rating]

if st.button("🎥 Pick Random Films"):
    if filtered_df.empty:
        st.error("No movies found with selected rating")
    else:
        films = get_random_films(filtered_df, num_films)

        # Dynamic layout based on number of films
        cols_per_row = 5
        rows = [films[i : i + cols_per_row] for i in range(0, len(films), cols_per_row)]

        for row in rows:
            cols = st.columns(len(row))
            for col, film in zip(cols, row):
                poster_url = get_poster_url(film["Movie Name"], film["Year of Release"])

                with col:
                    if poster_url:
                        st.image(poster_url, use_container_width=True)
                    else:
                        st.warning("Poster not available")

                    st.markdown(
                        f"""
                        ## 🎞️ {film['Movie Name']}
                        **📅 Year:** {film['Year of Release']}  
                        **⏱ Duration:** {film['Watch Time']}  
                        **⭐ Rating:** {film['Movie Rating']}  

                        **📚 Description:**  
                        {film['Description']}
                        """
                    )

        st.markdown("---")
