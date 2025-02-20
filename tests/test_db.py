from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import streamlit as st

from src.db import fetch_movies, get_poster_url, get_random_films


@pytest.fixture(autouse=True)
def mock_streamlit_secrets():
    """Mock Streamlit secrets globally for all tests"""
    with patch.object(st, "secrets", {"tmdb": {"api_key": "api_key"}}):
        yield


def test_get_poster_url():
    """Test get_poster_url with various scenarios"""
    movie_name = "Inception"
    expected_url = "https://image.tmdb.org/t/p/w780/Inception_2010.jpg"

    # Mock the requests.get call
    with patch("src.db.requests.get") as mock_get:
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 27205,
                    "title": "Inception",
                    "poster_path": "/Inception_2010.jpg",
                }
            ]
        }
        mock_get.return_value = mock_response

        # Test successful case
        result = get_poster_url(movie_name)
        assert result == expected_url

        # Verify API call
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        assert kwargs["params"]["api_key"] == "api_key"
        assert kwargs["params"]["query"] == movie_name


def test_get_poster_url_no_results():
    """Test get_poster_url when no results are found"""
    with patch("src.db.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": []}
        mock_get.return_value = mock_response

        result = get_poster_url("NonexistentMovie")
        assert result is None


def test_fetch_movies():
    """Test fetch_movies functionality"""
    with patch("src.db.requests.get") as mock_get:
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "results": [
                {
                    "id": 1,
                    "original_title": "Movie 1",
                    "poster_path": "/poster1.jpg",
                    "overview": "Description 1",
                },
                {
                    "id": 2,
                    "original_title": "Movie 2",
                    "poster_path": "/poster2.jpg",
                    "overview": "Description 2",
                },
            ]
        }
        mock_get.return_value = mock_response

        # Test with max_pages=1
        movies = fetch_movies(st.secrets["tmdb"]["api_key"], max_pages=1)

        # Verify results
        assert isinstance(movies, list)
        assert len(movies) == 2
        assert movies[0]["original_title"] == "Movie 1"
        assert movies[1]["original_title"] == "Movie 2"

        # Verify API call
        mock_get.assert_called_once_with(
            "https://api.themoviedb.org/3/discover/movie",
            params={
                "api_key": st.secrets["tmdb"]["api_key"],
                "sort_by": "vote_average.desc",
                "vote_count.gte": 300,
                "page": 1,
            },
        )


def test_fetch_movies_api_error():
    """Test fetch_movies when API returns an error"""
    with patch("src.db.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        movies = fetch_movies(st.secrets["tmdb"]["api_key"], max_pages=1)
        assert movies == []


@pytest.fixture
def sample_dataframe():
    """Fixture providing a sample DataFrame for testing"""
    data = {
        "original_title": ["Film A", "Film B", "Film C", "Film D", "Film E"],
        "overview": [
            "Action-packed movie.",
            "Drama with a twist.",
            "Thriller with suspense.",
            "Comedy adventure.",
            "Sci-fi epic.",
        ],
        "poster_path": [
            "/path1.jpg",
            "/path2.jpg",
            "/path3.jpg",
            "/path4.jpg",
            "/path5.jpg",
        ],
        "vote_average": [7.5, 8.0, 6.5, 7.0, 8.5],
    }
    return pd.DataFrame(data)


def test_get_random_films(sample_dataframe):
    """Test get_random_films with various scenarios"""
    # Test normal case
    num_films = 2
    random_films = get_random_films(sample_dataframe, num_films)

    assert len(random_films) == num_films
    for film in random_films:
        assert "original_title" in film
        assert "overview" in film
        assert "poster_path" in film
        assert "vote_average" in film

    # Test with num_films larger than DataFrame
    random_films = get_random_films(sample_dataframe, 10)
    assert len(random_films) == len(sample_dataframe)

    # Test with empty DataFrame
    empty_df = pd.DataFrame(columns=sample_dataframe.columns)
    random_films = get_random_films(empty_df, num_films)
    assert len(random_films) == 0
