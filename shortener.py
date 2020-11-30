import urllib
import requests
import random
import string

def is_valid(message):
    if  message[:4] != 'http':        
        message = 'http://' + message
    elif message[:8] == 'https://':
        message.replace(message[5], '')
    try:
        print(message)
        urllib.request.urlopen(message)              # проверка валидности ссылки
        return message[message.index('/') + 2 :]
    except Exception:
        return False

def reduce(message):
    message = is_valid(message)
    if message == False:
        return 'Ваша ссылка некорректна'
    elif message.index('.') >= 3:
        message = message[:3]
    else:
        message = message[:message.index('.')]
    message = message + ''.join(random.sample(string.ascii_lowercase + string.digits, random.randint(1, 2)))
    return 'redurl.xyz/' + message
