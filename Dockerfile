# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (Flask runs on 5000 by default)
EXPOSE 5000

# Command to run the application
CMD ["python","app.py"]
