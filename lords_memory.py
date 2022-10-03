import csv

import requests

url = "https://lordsmobile.igg.com/project/lordsmemory/ajax.php?game_id=1051029902"

headers = {
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"'
}


def send_claim_request(igg_id):
    payload = f'ac=get_receive&iggid={igg_id}&lang=en'

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def main():
    with open('name_igg_id.csv', 'r') as read_file:
        reader = csv.reader(read_file,  delimiter =':')
        for row in reader:
            send_claim_request(row[1].strip())


if __name__ == '__main__':
    main()
