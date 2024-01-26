# Use the official Python 3.8 image from the Docker Hub
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]


