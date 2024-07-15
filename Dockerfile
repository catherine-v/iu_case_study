# Use a base image with the desired dependencies
FROM python:3.12-slim

# Install system packages
RUN apt-get update && \
    apt-get install -y \
    gcc \
    git \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the source code into the container
COPY . /app

# Install the python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set main.py as the entrypoint
ENTRYPOINT ["python", "src/main.py"]
