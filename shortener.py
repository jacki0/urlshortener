import urllib
import requests
import random
import string

def is_valid(message):
    if message[:8] != 'https://' and message[:7] != 'http://':        
        message = 'http://' + message
    elif message[:8] == 'https://':
        message.replace(message[5], '')
    try:
        urllib.request.urlopen(message)              # проверка валидности ссылки
        return message[message.index('/') + 2 : message.index('.')]
    except Exception:
        return False
def reduce(message):
    message = is_valid(message)
    if message == False:
        return 'Ваша ссылка некорректна'
    elif len(message) >= 3:
        message = message[:3]
    message = message + ''.join(random.sample(string.ascii_lowercase + string.digits, random.randint(1, 10)))
    return 'tgshr.tk/' + message[:6]
