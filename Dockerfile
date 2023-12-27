FROM python:3.12-alpine3.19

COPY requirements.txt /temp/requirements.txt
COPY app /usr/src/app
COPY fixtures/db.json /usr/src/db.json

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password stripe-user

