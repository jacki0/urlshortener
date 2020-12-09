
FROM python:3.7.5

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt
