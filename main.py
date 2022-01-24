import csv
import urllib

import updateMembers
import requests
import json
from requests.sessions import Session


url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/87.0.4280.66 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def send_claim_code_request(gift_code, member_name, session):
    payload = f'ac=get_gifts&cdkey={urllib.parse.quote(gift_code)}&charname={member_name}&iggid=0&lang=en&type=1'
    with session.post(url, data=payload) as response:
        print(member_name, response.text)


def claim_for_users(gift_code, username_list):
    with requests.Session() as session:
        session.headers = headers

        for member in username_list:
            send_claim_code_request(gift_code, member, session)


def main(gift_code):
    list_files = ['members1.csv', 'members3.csv']
    for memberList in list_files:
        username_list = list()
        with open(memberList, 'r') as read_file:
            reader = csv.reader(read_file,  delimiter =':')
            for row in reader:
                username_list.append(row[1].strip())
        claim_for_users(gift_code, username_list)


if __name__ == '__main__':
    # claim multiple codes from a csv file.
    with open('active_codes.csv', "r") as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            code = row[0]
            main(code)
