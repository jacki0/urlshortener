from urllib.request import urlopen, Request
from pymongo import MongoClient
import datetime
import random
import string
import json


with open('bot/config.json') as file:
    config = json.load(file)
    host = config['host']
    port = config['port']

sample = string.ascii_lowercase + string.digits
client = MongoClient(host, port)
db = client.urls_db
collection = db.urls


def is_valid(orig_url):
    if orig_url[:4] != 'http':
        orig_url = 'http://' + orig_url
    elif orig_url[:8] == 'https://':
        orig_url.replace(orig_url[5], '')
    if orig_url[-1] == '/':
        orig_url = orig_url[:-1]
    req = Request(orig_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        urlopen(req).read()
        return orig_url[orig_url.index('/') + 2 :]
    except Exception as e:
        return orig_url[orig_url.index('/') + 2 :], e


def reduce(message):
    orig_url = is_valid(message)
    if type(orig_url) is not str:
        ex = orig_url[1]
        orig_url = orig_url[0]
    if orig_url.index('.') >= 3:
        reduced_url = orig_url[:3]
    else:
        reduced_url = orig_url[:orig_url.index('.')]
    reduced_url = 'redurl.xyz/' + reduced_url + ''.join(random.sample(sample, random.randint(1, 2)))
    try:
        ex
        return reduced_url, ex
    except NameError:
        return reduced_url


def insert_url(message):
    reduced_url = reduce(message)
    if type(reduced_url) is not str:
        ex = reduced_url[1]
        reduced_url = reduced_url[0]
    url = {"orig_url": message, "reduced_url": reduced_url, "date": str(datetime.datetime.now())[:-7]}
    try:
        try:
            ex
            return reduced_url, collection.insert_one(url).inserted_id, ex
        except NameError:
            return reduced_url, collection.insert_one(url).inserted_id
    except Exception as e:
        return e


def is_databased(col, uurl):
    for i in collection.find({col: uurl}):
        return i


def run(message):
    in_db = is_databased("orig_url", message)
    if in_db is not None:
        result = in_db["reduced_url"]
    else:
        result = insert_url(message)
        if type(result) is not tuple:
            log = {'exeption': [message, str(result), str(datetime.datetime.now())[:-7]]}
            result = 'Что-то пошло не так.\nПопробуйте снова.'
        elif len(result) == 2 and 'ObjectId' in str(type(result[1])):
            print(result)
            log = {'insert_id': [message, str(result[1]), str(datetime.datetime.now())[:-7]]}
            result = result[0]
        elif len(result) == 3:
            log = {'insert_id': [message, str(result[1]), str(result[1]), str(datetime.datetime.now())[:-7]]}
            result = [result[0], 'Ошибка проверки ссылки: ' + str(result[2]) + '. Проверьте корректность.']
        json.dump(log, open('log.json', 'a'), indent=0)
    return result
