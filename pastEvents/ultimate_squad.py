# QGH3QC Trickys team
# Gummi GummiMeUp Drottningen Kandylicious
# QA52R9 Shifty team
# MiniGummi Immug Immug2 GummiOres

import requests
team_one = {"TrickySavior": 456114621, "Gummi": 519568075, "GummiMeUp": 539030787, "Drottningen": 505506668,
            "Kandylicious": 458410987, "ShiftySavior": 512937877, "Immug": 855922161, "MiniGummi": 761678769,
            "Immug2": 680581361, "MatGummi": 526545099}

for name, iggID in team_one.items():
    with requests.session() as session:
        url = "https://lordsmobile.igg.com/event/ultimate_squad/ajax.php?game_id=1051029902"

        payload = 'ac=run_login&char_name=' + name + '&iggid=' + str(iggID) + '&lang=en'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }

        response = session.request("POST", url, headers=headers, data=payload)
        print(response.text)
        # for number in range(1, 5):
        payload = 'ac=run_task&lang=en&type=' + str(2)
        response = session.request("POST", url, headers=headers, data=payload)
        print(response.text)

# payload='ac=run_receive&id=8908&lang=en'
# payload='ac=run_receive&id=8960&lang=en'
# payload='ac=run_receive&id=8961&lang=en'