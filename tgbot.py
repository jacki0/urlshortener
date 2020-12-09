from shortener import run
import telebot
import json


with open('config.json') as file:
    config = json.load(file)
    key = config['bot_key']
