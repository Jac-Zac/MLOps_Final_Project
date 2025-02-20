import subprocess
import time

import pytest
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
        ],  # Headless mode
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Wait for Streamlit to be ready (increase sleep time if needed)
    time.sleep(5)

    yield  # Run tests

    # Cleanup: Terminate Streamlit after tests
    streamlit_process.terminate()
    streamlit_process.wait()


def test_app_loads():
    """Check if Streamlit app loads properly."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run Playwright in headless mode
        page = browser.new_page()

        # Try connecting to the app
        page.goto("http://localhost:8501", timeout=10000)  # Wait up to 10 sec

        browser.close()
