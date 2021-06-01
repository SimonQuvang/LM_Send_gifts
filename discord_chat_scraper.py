import requests
import json


def retrieve_messages(channel_id):
    headers = {'authorization': 'MjIzODQwNDAzMzUzMzcwNjI0.YLAsXQ.Yei9yynWi6TPtke2OjcVoTZvBKA'}

    req = requests.get(f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=headers)
    json_obj = json.loads(req.text)
    for value in json_obj:
        print(value, '\n')


retrieve_messages('844882189068926987')
