FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Expose port and run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
