import requests
from config import url
import json


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)

    return None


data = get_data(url)


def get_dollar_price(data):
    dollar_price = data['list'][0]['price']
    return dollar_price


each_dollar_to_rial = get_dollar_price(data)


def dollar_to_toman(dollar = 1):
    toman = (dollar * each_dollar_to_rial) // 10 
    return toman







