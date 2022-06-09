FROM python:3.9-slim

COPY ./api_music /app/api_music
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000