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

# Sidebar filters
with st.sidebar:
    st.markdown("## 🔍 Filter Movies")
    min_rating = st.slider("Minimum Rating", 0.0, 10.0, 7.0, 0.1)
    num_films = st.slider(
        "Number of Films", 1, 10, 3, key="num_films"
    )  # Slider for number of films

filtered_df = df[df["Movie Rating"].astype(float) >= min_rating]

# Random film selection button
st.markdown(
    """
    <style>
    .wide-button-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .wide-button {
        width: 100%;
        padding: 15px;
        font-size: 18px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "random_clicked" not in st.session_state:
    st.session_state.random_clicked = False

st.markdown('<div class="wide-button-container">', unsafe_allow_html=True)
if st.button(
    "🎲 Get Random Films", key="random_films", help="Click to discover random movies"
):
    st.session_state.random_clicked = True
st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.random_clicked:
    if filtered_df.empty:
        st.error("No movies found with selected rating")
    else:
        films = get_random_films(filtered_df, num_films)
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
                        f"**🎞️ {film['Movie Name']} ({film['Year of Release']})**"
                    )
                    st.markdown(f"⭐ {film['Movie Rating']} | ⏱ {film['Watch Time']}")
    st.markdown("---")

if not st.session_state.random_clicked:
    # Showcase of 5 random films
    st.markdown("## 🎥 Featured Movies")
    showcase_films = get_random_films(df, 5)
    cols = st.columns(len(showcase_films))

    for col, film in zip(cols, showcase_films):
        poster_url = get_poster_url(film["Movie Name"], film["Year of Release"])
        with col:
            if poster_url:
                st.image(poster_url, use_container_width=True)
            else:
                st.warning("Poster not available")
            st.markdown(f"**🎞️ {film['Movie Name']} ({film['Year of Release']})**")
            st.markdown(f"⭐ {film['Movie Rating']} | ⏱ {film['Watch Time']}")
    st.markdown("---")
