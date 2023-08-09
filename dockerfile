# Base image
FROM ubuntu:latest

# Define environment variable
ENV VERSION=1.2.0

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 vim git zip unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy files
COPY zip_job.py /tmp/

# Run command on container startup
CMD uname -a && file /tmp/zip_job.py
