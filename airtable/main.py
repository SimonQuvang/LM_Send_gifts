import api_keys

import os
from pprint import pprint
from airtable import Airtable
import csv
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

base_key = api_keys.baseId  # Insert the Base ID of your working base
table_name = 'Table 1'  # Insert the name of the table in your working base
api_key = api_keys.api_key  # Insert your API Key

table = Airtable(base_key, table_name, api_key)
project_root = os.path.dirname(os.path.dirname(__file__))


def update_might_table():
    members = table.get_all()
    pprint(members)
    for member in members:
        time.sleep(0.22)
        member_name = member['fields']['Member']
        old_might = "0"
        old_might = member['fields']['Might']
        old_might = re.sub(r'[^\w\s]', '', old_might)
        new_might = get_data_from_website(member_name)
        new_might_int = re.sub(r'[^\w\s]', '', new_might)
        might_change = "-1"
        if old_might is not '0' and new_might:
            might_change = int(new_might_int) - int(old_might)
            might_change = str(might_change)
            print(might_change)
        kingdom = get_kingdom(member_name)
        pprint(member)
        fields = {'Might': new_might, 'Kingdom': kingdom, "MightChange": might_change}
        table.update(member['id'], fields)
        print(member_name, new_might, kingdom)


def get_kingdom(player_name):
    session = HTMLSession()
    url = f'https://lordsmobilemaps.com/en/player/{player_name}'

    request = session.get(url)
    html = BeautifulSoup(request.text, 'lxml')
    if html.select('.playerdesc'):
        player_info = html.select('.playerdesc')[0]
        kingdom = player_info.select('a')[0].text.split('-')[0].split('#')[1]

        return kingdom
    else:
        return '-1'


def get_data_from_website(player_name):
    session = HTMLSession()
    url = f'https://lordsmobilemaps.com/en/player/{player_name}'

    request = session.get(url)

    html = BeautifulSoup(request.text, 'lxml')
    if html.select('.playerdesc'):
        player_info = html.select('.playerdesc')[0]
        kingdom = player_info.select('a')[0].text
        might_kills = player_info.select('p')[1].text

        might = might_kills.find('might')
        and_split = might_kills.find('and')

        might_string = might_kills[int(might): int(and_split)]
        m = re.search(r"\d", might_string)
        if m:
            might_number = might_string[m.start():]
            return might_number
        else:
            print(player_info)
            print(might_kills)
            print(might_string)
            return "-2"
    else:
        return '-1'


def read_data():
    with open(f'{project_root}\members3.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            member_name = row[0].strip()
            member_might = row[1].strip()
            update_might_table(member_name, member_might)
            time.sleep(0.4)
            print(member_name)


if __name__ == '__main__':
    update_might_table()
