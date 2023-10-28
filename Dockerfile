# Use Python 3.10 as the base image
FROM python:3.10

# Set the creator label
LABEL creator: "Deepak Mittal"

# Update the package list and install tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

# Copy everything into the container at root
COPY . /app/

# Set the working directory to /app2
WORKDIR /app

# Install the required Python packages
RUN pip install -r requirements.txt

# Make the start.sh script executable
RUN chmod +x start.sh

# Set the command to run the app using uvicorn and python app.py
CMD ["./start.sh"]