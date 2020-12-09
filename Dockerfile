
FROM python:3

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

CMD [ "/usr/bin/python3", "app/tgbot.py" ]
