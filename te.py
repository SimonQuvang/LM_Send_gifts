import csv
import logging
import threading
import time
import requests

url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.66 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
with requests.Session() as s:
    requests.get(url)
    for id in range(100153096, 499999999):
        payload='ac=get_gifts&cdkey=lm001&charname=&iggid=' + str(id) + '&lang=en&type=0'
        response = s. (data=payload)
        print(response.text)