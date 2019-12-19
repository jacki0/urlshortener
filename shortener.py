import urllib
import requests

def is_valid(message):
    if message[:8] != 'https://' and message[:7] != 'http://':        
        message = 'http://' + message
    print(message)
    try:
        urllib.request.urlopen(message)              # проверка валидности ссылки
        return True
    except Exception:
        return False
