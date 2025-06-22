# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY requirements.txt .
COPY srcapp.py ./src/
COPY srcmodel.py ./src/
COPY srctrain.py ./src/
COPY .github/workflows/workflows.yaml .github/workflows/

# Default command (training)
CMD ["python", "src/train.py"]

# For Gradio (uncomment if needed):
# CMD ["python", "src/app.py"]
