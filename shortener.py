from pymongo import MongoClient
import datetime
import requests
import random
import urllib
import string
import json


with open('config.json') as file:
    config = json.load(file)
    host = config['host']
    port = config['port']

sample = string.ascii_lowercase + string.digits

client = MongoClient(host, port)
db = client.urls_db
collection = db.urls


def is_valid(orig_url):
    if  orig_url[:4] != 'http':        
        orig_url = 'http://' + orig_url
    elif orig_url[:8] == 'https://':
        orig_url.replace(orig_url[5], '')
    try:
        urllib.request.urlopen(orig_url)
        return orig_url[orig_url.index('/') + 2 :]
    except Exception:
        return False


def reduce(message):
    orig_url = is_valid(message)
    if not orig_url:
        return 'Ваша ссылка некорректна'
    elif orig_url.index('.') >= 3:
        reduced_url = orig_url[:3]
    else:
        reduced_url = orig_url[:orig_url.index('.')]
    reduced_url = 'redurl.xyz/' + reduced_url + ''.join(random.sample(sample, random.randint(1, 2)))
    return reduced_url


url = {"orig_url": message,
          "reduced_url": reduce(message),
          "date": str(datetime.datetime.now())[:-7]}
url_id = collection.insert_one(url).inserted_id
