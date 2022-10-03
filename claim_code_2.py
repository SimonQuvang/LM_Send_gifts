import csv
import urllib
import updateMembers
import requests

url = "https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902"
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/87.0.4280.66 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def send_claim_code_request(gift_code, igg_id, session):
    payload = f'ac=get_gifts&cdkey={urllib.parse.quote(gift_code)}&charname=&iggid={igg_id}&lang=en&type=0'
    with session.post(url, data=payload) as response:
        print(igg_id, response.text)


def main():
    gift_code = 'LMSMILEY'
    with requests.Session() as session:
        session.headers = headers
        with open('name_igg_id.csv', 'r') as read_file:
            reader = csv.reader(read_file,  delimiter =':')
            for row in reader:
                send_claim_code_request(gift_code, row[1].strip(), session)


if __name__ == '__main__':
    main()
