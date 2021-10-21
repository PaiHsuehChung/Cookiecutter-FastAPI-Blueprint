FROM python:3.8.10-slim-buster

ENV TYPE=backend
ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y git

WORKDIR $WORKDIR

RUN pip install --upgrade pip
COPY requirements_dev.txt requirements_dev.txt
RUN pip install -r requirements_dev.txt

RUN adduser --system --group $USER
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME
USER $USER

EXPOSE {{ cookiecutter.application_port }}