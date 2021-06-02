from requests_html import HTMLSession
import chompjs
from bs4 import BeautifulSoup
import csv

session = HTMLSession()
url = 'https://lordsmobilemaps.com/en/alliance/Night+Raid'

request = session.get(url)

html = BeautifulSoup(request.text, 'lxml')
guild_info = html.select('div.detaildedbody')[2]
guild_members = guild_info.select('div.toptabrow div:nth-child(2) a')

members = []
for member in guild_members:
    members.append(member.string)

with open('members3.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=":")
    for m in members:
        row = ['member', m]
        writer.writerow(row)
