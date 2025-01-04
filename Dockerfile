# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system-level dependencies for face_recognition
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    gcc \
    g++ \
    make \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    libboost-thread-dev \
    libjpeg-dev \
    libpng-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Start FastAPI using uvicorn
CMD ["uvicorn", "app.backend:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
