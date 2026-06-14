FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Flask
RUN pip install flask

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
