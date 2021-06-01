import csv

import requests

url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.66 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def claim_key(code, listFile):
    with open(listFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            member = row[1].strip()
            payload = f'ac=get_gifts&cdkey={key}&charname={member}&iggid=0&lang=en&type=1'
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)


key = '8H3XBWXA'
list_files = ['members1.csv','members2.csv','members3.csv']
for memberList in list_files:
    with open('codes.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            key = row[0]
            claim_key(key, memberList)