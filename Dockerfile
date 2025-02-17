# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy the source code
COPY src/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the required port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]

