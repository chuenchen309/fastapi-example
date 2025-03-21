FROM python:3.12-slim-bullseye as builder
# FROM --platform=linux/amd64 python:3.11-slim-buster as build

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "./run.py"]
