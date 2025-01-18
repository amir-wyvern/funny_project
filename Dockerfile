# Use an official Python runtime as a parent image
FROM python:3.10-slim

ARG BOT_TOKEN
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BOT_TOKEN=$BOT_TOKEN

CMD ["python", "main.py"]
