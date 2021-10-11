import requests
from time import sleep

prev = 0
while True:
    req = requests.get('http://127.0.0.1:8000/api')
    status = req.text
    if status == '1' and status != prev:
        print("lights on")
    elif status == '0' and status != prev:
        print("lights of")
    prev = status
    sleep(0.5)