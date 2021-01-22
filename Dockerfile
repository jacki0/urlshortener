
FROM python:3.7

WORKDIR /

ADD . /

RUN pip3 install -r requirements.txt

RUN chmod +x tgbot.py