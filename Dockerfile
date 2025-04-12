# Use an official Python runtime as a parent image
FROM python:3.10-slim

ARG BOT_TOKEN

ARG HTTP_PROXY
ARG HTTPS_PROXY
ENV HTTP_PROXY=$HTTP_PROXY \
    HTTPS_PROXY=$HTTPS_PROXY \
    http_proxy=$HTTP_PROXY \
    https_proxy=$HTTPS_PROXY

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

# Unset proxy environment variables for runtime
ENV HTTP_PROXY="" \
    HTTPS_PROXY="" \
    http_proxy="" \
    https_proxy=""


ENV BOT_TOKEN=$BOT_TOKEN

CMD ["python", "main.py"]
