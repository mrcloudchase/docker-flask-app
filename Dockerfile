# syntax=docker/dockerfile:1

FROM python:3.13-alpine

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set a working directory
WORKDIR /app

# Copy only requirements
COPY requirements.txt .

# Install dependencies without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY app.py .

# Switch to non-root user
USER appuser

# Expose port 5000
EXPOSE 5000

# Set environment variable
ENV FLASK_ENV=production

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s\
  CMD wget --no-verbose --tries=1 --spider http://127.0.0.1:5000/health || exit 1

# Start the Flask application
CMD ["python", "app.py"]
