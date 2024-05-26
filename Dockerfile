# Use an official Python runtime as a parent image
FROM python:3.10-alpine3.17

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 to allow communication to/from the Flask app
EXPOSE 5001

# Define environment variable for Flask to run in development mode
ENV FLASK_ENV=development

# Run app.py when the container launches, specifying the host and port explicitly
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
