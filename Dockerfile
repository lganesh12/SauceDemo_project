# Use the official Playwright Python image
FROM mcr.microsoft.com/playwright/python:v1.52.0

# Set working directory
WORKDIR /tests

# Copy requirements first to cache dependencies
COPY requirement.txt .

# Install Python dependencies
RUN pip install -r requirement.txt

# Copy test files
COPY . .

# Default command to run tests
CMD ["behave"]