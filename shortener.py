import urllib
import requests
import random
import string

def is_valid(message):
    if message[:8] != 'https://' and message[:7] != 'http://':        
        message = 'http://' + message
    try:
        urllib.request.urlopen(message)              # проверка валидности ссылки
        return message
    except Exception:
        return False

def reduce(message):
    message = is_valid(message)
    if message == False:
        return 'Ваша ссылка некорректна'
    message = message[message.index('/') + 2 : message.index('.')]
    if len(message) >= 3:
        message = message[:random.randint(2, 4)]
    message = 'tgshr.tk/' + message + ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 3)))
    return message
