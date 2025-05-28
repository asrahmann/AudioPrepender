FROM python:3.11-slim

WORKDIR /app

# Install system dependencies and Python packages
RUN apt-get update && \
    apt-get install -y ffmpeg gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Tell Flask which app to run
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
