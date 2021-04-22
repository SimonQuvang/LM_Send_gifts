import requests
import random
import csv
from fake_useragent import UserAgent
import concurrent.futures

# opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

with open('proxy.csv', 'r') as f:
    reader = csv.reader(f, delimiter =',' )
    for row in reader:
        proxylist.append(row[0])


def extract():
    proxy = random.choice(proxylist)
    url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    payload = 'ac=get_gifts&cdkey=lm001&charname=&iggid=' + str(100003300) + '&lang=en&type=0'
    try:
        # change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get("https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902", data=payload, headers=headers, proxies={'http': proxy}, timeout=2)
        print(r.text)
    except:
        print('dosent work')
        pass
    return proxy


print(extract())