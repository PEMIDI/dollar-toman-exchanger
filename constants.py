import requests
from config import URL_CURRENCY
import json


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)

    return None


def get_currency(data):
    return data['list']


def dollar_to_rial(price_dollar, value_dollar=1):
    return value_dollar * price_dollar


def import_data_to_file(currency, time):
    list_currency = list()

    for i in currency:
        list_currency.append(f'{i["nameFa"]}: {i["price"]}')

    with open(f'archive/currency.json', 'w') as f:
        f.writelines(json.dumps(list_currency))


json_data = get_data(URL_CURRENCY)
all_currency = get_currency(json_data)
timeUpdate = json_data['timeUpdate'][0]
import_data_to_file(all_currency, timeUpdate)
price_dollar = all_currency[0]['price']

