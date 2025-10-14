# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (gunicorn will run on this)
EXPOSE 8000

# Run database migrations + start gunicorn
CMD python manage.py migrate && \
    pytest tests/ && \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
