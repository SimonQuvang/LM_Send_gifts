import requests
import csv
url = "https://lordsmobile.igg.com/project/rally_on/ajax.php?game_id=1051029902"


with open('account_name_iggid.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        member = row[0].strip()
        igg_id = str(row[1]).strip()
        with requests.Session() as s:
            payload = 'ac=run_login&char_name=' + member + '&iggid=' + igg_id + '&lang=en'
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'rally_on_iggid=' + igg_id
            }

            response = s.request("POST", url, headers=headers, data=payload)
            print(response.text)
            for number in range(1, 7):
                payload = 'ac=receive_prize&lang=en&type=' + str(number)
                response = s.request("POST", url, headers=headers, data=payload)
                print(response.text)
