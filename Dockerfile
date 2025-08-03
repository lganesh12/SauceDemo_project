# Use official Python image with Node.js for Playwright support
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirement.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirement.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Copy test files
COPY . .

# Set default command to run Behave tests
CMD ["behave"]
