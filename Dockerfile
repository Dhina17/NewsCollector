# Python base docker image
FROM python:3.9-slim-buster

# Specify the work directory
WORKDIR /app

# Copy the requirements.txt to work directory
COPY requirements.txt .

# Install required modules using pip3
RUN pip3 install -r requirements.txt

# Copy all the remaining files to work directory
COPY . .

# Execute the main.py file.
CMD ["python3", "main.py"]