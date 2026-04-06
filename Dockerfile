FROM python:3.10-slim

WORKDIR /app

# Copy dependencies needed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the API Port for HuggingFace Spaces
EXPOSE 7860

# Run the FastAPI server precisely executing Space validation parameters
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
