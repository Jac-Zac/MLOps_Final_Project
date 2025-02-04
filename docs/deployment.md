# Deployment Guide

This document explains how to deploy the **PickaFilm** app using Docker and GitHub Actions. The code resides in the `src/` directory.

## Local Deployment with Docker

Containerizing the app ensures consistency across environments.

### Building the Docker Image

1. **Navigate to the project root** where the `Dockerfile` is located.
2. **Build the image** by running:
   ```bash
   docker build -t pickafilm:latest .
   ```

### Running the Docker Container Locally

To run the container and map its port 8501 to your local machine:

```bash
docker run -p 8501:8501 pickafilm:latest
```

Then, open your browser at [http://localhost:8501](http://localhost:8501) to view the app.

## CI/CD Deployment with GitHub Actions

The GitHub Actions workflow automates testing, building the Docker image, and pushing it to a container registry when you create a new release tag.

### Workflow Overview

- **Location:** `.github/workflows/ci-cd.yml`
- **Triggers:**
  - The workflow runs on pushes to the `main` branch and on pull requests for continuous integration.
  - When a tag (e.g., `v1.0.0`) is pushed, the workflow builds and pushes the Docker image to the GitHub Container Registry.

### Key Steps in the Workflow

1. **Checkout Code:**  
   The workflow checks out the code from the repository.

2. **Set Up Python and Install Dependencies:**  
   It installs the required dependencies and runs tests using `pytest`.

3. **Build and Push Docker Image:**  
   When a new tag is detected, the workflow builds the Docker image and pushes it to the container registry with both `latest` and version-specific tags.

### Creating a Release

To trigger the deployment workflow:

1. **Tag Your Release:**

   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **GitHub Actions Workflow:**  
   After the tag is pushed, GitHub Actions automatically builds and pushes the Docker image.

## Additional Considerations

- **Secrets and Credentials:**  
  Make sure your repository has the necessary secrets set up (e.g., `GITHUB_TOKEN` for authenticating with the GitHub Container Registry).

- **Environment Variables:**  
  If your app requires additional environment variables, configure them in your Dockerfile or pass them at runtime.

This guide outlines the key steps for deploying the app both locally and via CI/CD. Adjust these instructions as needed to fit your specific deployment environment and requirements.
