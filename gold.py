import requests
from config import URL_GOLD
import json


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)

    return None


def get_gold(data):
    return data['list']


def gold_coin(price_golds, value_gold=1):
    return (price_golds * value_gold)


def import_data_to_file(currency, time):
    list_currency = list()

    for i in currency:
        list_currency.append(f'{i["name"]}: {i["price"]}')

    with open(f'archive/gold.json', 'w') as f:
        f.writelines(json.dumps(list_currency))


json_data = get_data(URL_GOLD)
all_gold = get_gold(json_data)
timeUpdate = json_data['timeUpdate'][0]
price_gold = all_gold[0]['price']
import_data_to_file(all_gold, timeUpdate)

