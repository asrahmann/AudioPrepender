FROM python:3.11-slim

WORKDIR /app

# --network=host is REMOVED from this RUN command
RUN apt-get update && \
    apt-get install -y ffmpeg gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# It's good practice to install requirements before copying the rest of the app
# This leverages Docker's layer caching more effectively.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
