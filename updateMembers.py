from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv


def cleanup():
    open("members3.csv", "w").close()  # Cleans the file so we get no duplicates


def add_member(member):
    with open('members3.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(member)


def get_data_from_website(guild_name):
    session = HTMLSession()
    url = f'https://lordsmobilemaps.com/en/alliance/{guild_name}'

    request = session.get(url)

    html = BeautifulSoup(request.text, 'lxml')
    guild_info = html.select('div.detaildedbody')[2]

    guild_members_list = guild_info.select('div.toptabrow')

    for member in guild_members_list:
        member_name = member.select('div:nth-child(2) a')[0].string
        member_might = member.select('div:nth-child(5)')[0].string
        member_kills = member.select('div:nth-child(6)')[0].string
        member_kingdom = member.select('div:nth-child(3)')[0].string

        row = [member_name, member_might, member_kills,member_kingdom]
        add_member(row)


def get_member_data(guild_name):
    get_data_from_website(guild_name)


def main(guild_name):
    cleanup()
    get_member_data(guild_name)


if __name__ == '__main__':  # Makes it possible to run this code standalone
    main("Guild+without+Name")
