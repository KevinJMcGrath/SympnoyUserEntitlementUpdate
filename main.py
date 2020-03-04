import jsonpickle
import requests.exceptions

import config

from symphony import BotClient

bot = BotClient(config.bot_config)

user_list = jsonpickle.decode(bot.Admin.list_users())
user_id_list = [str(user['userSystemInfo']['id']) for user in user_list if user['userSystemInfo']['status'] == 'ENABLED']

# entitlement is intentionally misspelled.
meeting_link_feature = {"entitlment": "canFetchMeetingLinks", "enabled": True}

for user_id in user_id_list:
    response = None

    try:
        response = bot.Admin.update_user_features(user_id, [meeting_link_feature])
        print(f'{user_id} updated.')
    except requests.exceptions.HTTPError as http_ex:
        print(f'{user_id} was not updated. Error: {http_ex}')

        if response and response.text:
            print(f'Response: {response.text}')
    except Exception as ex:
        print(f'{user_id} was not updated. Error: {ex}')
