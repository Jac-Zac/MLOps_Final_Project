# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app/

# Create and activate virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies in virtual environment
RUN . /app/venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Expose the required port
EXPOSE 8501

# Run the application
CMD ["/app/venv/bin/streamlit", "run", "/app/src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
