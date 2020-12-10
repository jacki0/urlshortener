
FROM python:3.7

WORKDIR /

ADD . /

RUN pip3 install -r requirements.txt

RUN python3 tgbot.py
