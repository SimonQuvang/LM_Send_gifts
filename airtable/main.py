from pyairtable import Table, Base
import pprint
import csv

pp = pprint.PrettyPrinter(width=41, compact=True)
base_key = "appqS5f1NDO9lgDUF"  # Insert the Base ID of your working base
table_name = 'tbls4xmGpnFmf3fIV'  # Insert the name of the table in your working base
api_key = "keyke83QhDFZeUw1d"  # Insert your API Key


def get_might():
    members = {}
    with open('NRR-03.07.2022.csv', 'r') as read_file:
        reader = csv.reader(read_file, delimiter=',')
        for row in reader:
            user_id = row[2]
            members[user_id] = {
                "might": row[4],
                "kills": row[5],
                "troops_killed": row[13],
                "troops_lost": row[15],
                "troops_wounded": row[17],
                "enemy_troops_wounded": row[18],
                "enemies_destroyed_might": row[21],
                "enemies_captured": row[24],
                "prisoners_executed": row[25],
                "prisoners_escaped": row[26],
                "leaders_escaped": row[27],
                "leaders_captured": row[28],
                "leaders_executed": row[29],
                "bounty": row[30],
                "food_sent": row[34],
                "stones_sent": row[35],
                "timber_sent": row[36],
                "ore_sent": row[37],
                "gold_sent": row[38],
                "help_sent": row[39],
                "total_ress": row[40]
            }

    return members


def update_might_table(member_dict):
    table = Table(api_key, base_key, table_name)
    for member in table.all(formula="NOT({IGG ID}='')"):
        member_record_id = member['id']
        member_igg_id = member['fields']['IGG ID']
        if member_igg_id in member_dict:
            member_dict_iggid = member_dict[member_igg_id]
            might_change = '0'
            kills_change = '0'
            print(member['fields'])
            current_might = int(member['fields']["Might"].replace(',',''))
            new_might = int(member_dict_iggid["might"].replace(',', ''))
            if current_might != new_might:
                might_change = str(current_might - new_might)
            if member_dict_iggid["kills"] != member['fields']['Kills']:
                kills_change = str(
                    int(member_dict_iggid["kills"].replace(',', '')) - int(member['fields']['Kills'].replace(',', '')))
            table.update(member_record_id,
                         {
                             "Might": member_dict_iggid["might"],
                             "Might Change": might_change,
                             "Kills": member_dict_iggid["kills"],
                             "Kills Change": kills_change,
                             "Troops Killed": member_dict_iggid["troops_killed"],
                             "Troops Lost": member_dict_iggid["troops_lost"],
                             "Troops Wounded": member_dict_iggid["troops_wounded"],
                             "Enemy Troops Wounded": member_dict_iggid["enemy_troops_wounded"],
                             "Enemies Destroyed (Might)": member_dict_iggid["enemies_destroyed_might"],
                             "Enemies Captured": member_dict_iggid["enemies_captured"],
                             "Prisoners Executed": member_dict_iggid["prisoners_executed"],
                             "Prisoners Escaped": member_dict_iggid["prisoners_escaped"],
                             "Leaders Escaped": member_dict_iggid["leaders_escaped"],
                             "Leaders Captured": member_dict_iggid["leaders_captured"],
                             "Leaders Executed": member_dict_iggid["leaders_executed"],
                             "Bounty Collected": member_dict_iggid["bounty"],
                             "Food Sent": member_dict_iggid["food_sent"],
                             "Stones Sent": member_dict_iggid["stones_sent"],
                             "Timber Sent": member_dict_iggid["timber_sent"],
                             "Ore Sent": member_dict_iggid["ore_sent"],
                             "Gold Sent": member_dict_iggid["gold_sent"],
                             "Help Sent": member_dict_iggid["help_sent"],
                             "Total Resources Gathered": member_dict_iggid["total_ress"]
                         }
                         )


if __name__ == '__main__':
    members = get_might()
    update_might_table(members)
