# test_db.py
import pandas as pd
import pytest

from db import get_poster_url, get_random_films


def test_get_poster_url():
    movie_name = "Inception"
    expected_url = "https://image.tmdb.org/t/p/w500/Inception_2010.jpg"
    assert get_poster_url(movie_name) == expected_url


def test_get_random_films():
    # Create a small sample dataframe
    data = {
        "original_name": ["Film A", "Film B", "Film C"],
        "average_rating": [8.0, 7.5, 9.0],
        "Description": ["Desc A", "Desc B", "Desc C"],
    }
    df = pd.DataFrame(data)

    # Request 2 films from the 3 available
    films = get_random_films(df, 2)
    assert len(films) == 2
    # Ensure the films exist in our sample data
    sample_names = set(data["original_name"])
    for film in films:
        assert film["original_name"] in sample_names

    # Request more films than available
    films_all = get_random_films(df, 5)
    assert len(films_all) == 3  # Should return all available films
