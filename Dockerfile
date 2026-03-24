# Use a specific, stable Python 3.12 image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
# Adding a timeout and extra index can help if the connection is slow
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# The Magic Command (ensure 'metiquest' matches your project folder name)
CMD ["bash", "-c", "python manage.py migrate --noinput && python createsuperuser.py && gunicorn metiquest.wsgi:application --bind 0.0.0.0:8000"]