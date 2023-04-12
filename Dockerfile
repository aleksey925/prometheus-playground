FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY src/main.py /app

EXPOSE 8000
