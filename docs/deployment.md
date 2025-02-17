# Deployment Guide

This document explains how to deploy the **PickaFilm** app using Docker. The code resides in the `src/` directory.

## Local Deployment with Docker

Containerizing the app ensures consistency across environments.

### Building the Docker Image

1. **Navigate to the project root** where the `Dockerfile` is located.
2. **Build the image** by running:
   ```bash
   docker build -t pickafilm:latest .
   ```

### Running the Docker Container Locally

To run the container and map its port **8501** to your local machine:

```bash
docker run -p 8501:8501 pickafilm:latest
```

Then, open your browser at http://local host:8501 to view the app.

## Running the App Without Docker

If you prefer to run the app directly without using Docker:

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   streamlit run src/main.py
   ```

## Additional Considerations

- **Secrets and Credentials:**
  Ensure any required secrets are configured, such as API keys inside `.streamlit/secrets.toml`, referring to `sample_secrets.toml`.
