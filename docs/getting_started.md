# Getting Started with PickaFilm

This guide walks you through setting up **PickaFilm** on your local machine.

## Prerequisites

Ensure you have the following installed:

- **Python 3.11+**
- **pip** (Python package manager)
- **Docker** (optional, for containerized deployment)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jac-Zac/PickaFilm
cd PickaFilm
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv .env
source .env/bin/activate  # On Windows, use: .env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Running Locally

To start the **Streamlit** application:

```bash
streamlit run src/app.py
```

This will open the app in your default browser.

### Running with Docker

To build and run the app in a Docker container:

```bash
docker build -t pickafilm .
docker run -p 8501:8501 pickafilm
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Running Tests

Before pushing changes, ensure all tests pass:

```bash
pytest
```

## Contribution Guidelines

If you'd like to contribute, check out the [Development Guide](development.md).
