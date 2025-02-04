# Architecture Overview

The **PickaFilm** app is designed with a modular architecture to ensure separation of concerns, scalability, and ease of maintenance. This document explains how the different components interact.

## Components

- **Streamlit App (UI Layer)**

  - **Location:** `src/app.py`
  - **Purpose:**  
    Provides the user interface for the application. It handles user interactions—such as clicking the "Pick a Film" button—and displays film details returned from the backend.

- **Database Module (Data Access Layer)**

  - **Location:** `src/db.py`
  - **Purpose:**  
    Loads the film data from a CSV file (`data/films.csv`) and provides a function to return a random film. This separation makes it easier to change the data source in the future if needed.

- **Containerization**

  - **Location:** `Dockerfile` in the project root.
  - **Purpose:**  
    Contains instructions to build a Docker image for the app. Containerization ensures that the app runs consistently across various environments by packaging the code, dependencies, and runtime into one portable unit.

- **CI/CD Pipeline**
  - **GitHub Actions Workflow:** `.github/workflows/ci-cd.yml`
  - **Purpose:**  
    Automates testing, building, and deploying the application. The workflow runs tests on every push or pull request and builds the Docker image when a new version tag is created.

## How It Works Together

1. **User Interaction:**  
   The user accesses the Streamlit app and clicks the "Pick a Film" button.

2. **Data Retrieval:**  
   The app (in `src/app.py`) calls the `get_random_film()` function from `src/db.py`, which reads the CSV file and randomly selects a film.

3. **Display:**  
   The selected film's details are displayed on the UI.

4. **Deployment & Automation:**  
   The Docker container packages the entire application. GitHub Actions automates testing and image building, streamlining the deployment process.

This layered architecture makes it easier to maintain and extend the app. For example, updating the UI or changing the data source requires minimal changes to the other components.
