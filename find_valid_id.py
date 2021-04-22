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
# made it to id 100229757
if __name__ == '__main__':
    s = requests.Session()
    for id in range(500604267, 999999999):
        url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
        payload = 'ac=get_gifts&cdkey=lm001&charname=&iggid=' + str(id) + '&lang=en&type=0'
        r = s.post(url, data=payload, headers=headers)
        if not 'This IGG ID does not exist, or the game is under maintenance!' in r.text:
            with open('vaild_id2.csv', 'a') as file:
                file.write(str(id) + '\n')
        print(r.text + ' ' + str(id))
