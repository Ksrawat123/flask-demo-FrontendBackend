# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install into working directory as /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files into the directory
COPY . .

# Expose backend port
EXPOSE 9000

# Run the Flask app
CMD ["python", "app.py"]
