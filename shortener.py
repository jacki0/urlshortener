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
    except Exception as e:
        return orig_url, e


def reduce(message):
    orig_url = is_valid(message)
    if  type(orig_url) is not str:
        return orig_url
    elif orig_url.index('.') >= 3:
        reduced_url = orig_url[:3]
    else:
        reduced_url = orig_url[:orig_url.index('.')]
    reduced_url = 'redurl.xyz/' + reduced_url + ''.join(random.sample(sample, random.randint(1, 2)))
    return reduced_url


def insert_url(message):
    reduced_url = reduce(message)
    if type(reduced_url) is not str:
        return reduced_url
    else:
        url = {"orig_url": message,
                  "reduced_url": reduced_url,
                  "date": str(datetime.datetime.now())[:-7]}
        try:
            return reduced_url, collection.insert_one(url).inserted_id
        except Exception as e:
            return reduced_url, e


def run(message):
    result = insert_url(message)
    if type(result[1]) is str:
        log = {'insert_id' : [message, str(result[1]), str(datetime.datetime.now())[:-7]]}
    else:
        log = {'exeption' : [message, str(result[1]), str(datetime.datetime.now())[:-7]]}
    json.dump(log, open('log.json', 'a'), indent=0)
    return result[0]
