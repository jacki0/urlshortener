import urllib
import requests
import random
import string


sample = string.ascii_lowercase + string.digits


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
