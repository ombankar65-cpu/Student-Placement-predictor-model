# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies (optional but useful)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# If requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt || true

# If requirements.txt doesn't exist, fallback install
RUN pip install --no-cache-dir \
    numpy pandas scikit-learn matplotlib seaborn jupyter

# Expose port (for notebook or app)
EXPOSE 8888

# Default command (Jupyter Notebook)
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
