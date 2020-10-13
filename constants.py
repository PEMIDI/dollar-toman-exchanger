import requests
from config import url
import json


def get_data(url):
    response = requests.get(url)
    return json.loads(response.text)


data = get_data(url)


def get_dollar_price(data):
    
    return data['list'][0]['price']


each_dollar = get_dollar_price(data)


def dollar_to_rial(dollar = 1):
    return dollar * each_dollar







