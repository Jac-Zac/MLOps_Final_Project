from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import streamlit as st

from src.db import fetch_movies, get_poster_url, get_random_films


def test_get_poster_url():
    movie_name = "Inception"
    expected_url = "https://image.tmdb.org/t/p/w780/Inception_2010.jpg"

    # Patch the requests.get method used within src.db instead of the global one.
    with patch("src.db.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [{"poster_path": "/Inception_2010.jpg"}]
        }
        mock_get.return_value = mock_response

        assert get_poster_url(movie_name) == expected_url


@patch("src.db.requests.get")
@patch.object(st, "secrets", {"tmdb": {"api_key": "fake_api_key"}})
def test_fetch_movies(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [{"original_title": "Movie 1", "poster_path": "/poster1.jpg"}]
    }
    mock_get.return_value = mock_response

    # Use the API key from Streamlit secrets
    api_key = st.secrets["tmdb"]["api_key"]
    movies = fetch_movies(api_key, max_pages=1)
    assert isinstance(movies, list)
    assert len(movies) == 1
    assert movies[0]["original_title"] == "Movie 1"

    # Verify the correct API call was made
    mock_get.assert_called_with(
        "https://api.themoviedb.org/3/discover/movie",
        params={
            "api_key": api_key,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 500,
            "page": 1,
        },
    )


@pytest.fixture
def sample_dataframe():
    data = {
        "original_title": ["Film A", "Film B", "Film C"],
        "overview": [
            "Action-packed movie.",
            "Drama with a twist.",
            "Thriller with suspense.",
        ],
    }
    return pd.DataFrame(data)


def test_get_random_films(sample_dataframe):
    num_films = 2
    random_films = get_random_films(sample_dataframe, num_films)

    assert len(random_films) == num_films
    assert all("original_title" in film for film in random_films)
    assert all("overview" in film for film in random_films)
