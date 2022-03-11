FROM python:3.9-alpine

RUN pip install pipenv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROJECT_DIR /usr/src/app
ENV API_DIR ${PROJECT_DIR}/api

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

WORKDIR ${PROJECT_DIR}
RUN pipenv install --system --dev
COPY ./app ${API_DIR}/


