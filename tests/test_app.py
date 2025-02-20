import subprocess
import time

import pytest
import requests
from playwright.sync_api import sync_playwright

# Global variable for the Streamlit process
streamlit_process = None


@pytest.fixture(scope="module", autouse=True)
def start_streamlit():
    """Start the Streamlit app before running tests."""
    global streamlit_process
    streamlit_process = subprocess.Popen(
        [
            "streamlit",
            "run",
            "src/app.py",
            "--server.headless",
            "true",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Poll until the Streamlit app is responsive
    for _ in range(30):  # up to 60 seconds (30*2 sec)
        try:
            resp = requests.get("http://localhost:8501")
            if resp.status_code == 200:
                break
        except requests.exceptions.RequestException:
            pass
        time.sleep(2)
    else:
        pytest.fail("Timeout waiting for Streamlit app to start.")

    yield  # Run tests

    # Cleanup: Terminate Streamlit after tests
    streamlit_process.terminate()
    streamlit_process.wait()


def test_app_loads():
    """Check if Streamlit app loads properly."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501", timeout=30000)

        # Wait for the "Search for a movie" element with extended timeout
        page.wait_for_selector("text=Search for a movie", timeout=60000)

        assert "Search for a movie" in page.content()
        browser.close()


def test_search_functionality():
    """Test if the search functionality works correctly."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501", timeout=30000)

        # Wait for the search box to be visible with extended timeout
        search_box = page.locator("input[type='text']")
        search_box.wait_for(state="visible", timeout=60000)
        search_box.fill("Inception")
        page.keyboard.press("Enter")

        # Wait for search results to load
        page.wait_for_selector("text=Search Results", timeout=60000)

        assert "Search Results" in page.content()
        browser.close()


def test_random_movie_selection():
    """Test if clicking 'Get Random Films' shows results."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501", timeout=30000)

        # Wait for and click on the "Get Random Films" button
        random_button = page.locator("text=Get Random Films")
        random_button.click(timeout=60000)
        time.sleep(3)  # Allow extra time for movies to be displayed

        assert "Discover Random Films" in page.content()
        browser.close()
