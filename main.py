from constants import dollar_to_rial, price_dollar
from gold import gold_coin, price_gold
from time import sleep
import json


def exchanger_currency():
    number_of_dollars = int(input('how much dollar you have? '))

    result = dollar_to_rial(price_dollar, number_of_dollars)

    print(f"{number_of_dollars} ِDollar(USD) = {result} Rial(IRR)")
    sleep(3)
    menu()


def exchanger_gold():
    number_of_gold = int(input('how much gold coin you have? '))

    result = gold_coin(price_gold, number_of_gold)

    print(f"{number_of_gold} Gold Coin = {result} Rial(IRR)")
    sleep(3)
    menu()


def show_currency():
    with open('archive/currency.json', 'r') as f:
        data = json.loads(f.read())

        for i in data:
            print(i)
            sleep(0.25)

    sleep(3)
    menu()


def show_gold():
    with open('archive/gold.json', 'r') as f:
        data = json.loads(f.read())

        for i in data:
            print(i)
            sleep(0.25)

    sleep(3)
    menu()


def menu():
    show_menu = True

    while show_menu:
        choice = input('1. for exchange USD to IRR press (1)\n'
                       '2. for see price currency press (2)\n'
                       '3. for see price golds press (3)\n'
                       '4. for see how many coins cost a few Rials press (4)\n'
                       '5. for exit press (e)\n'
                       'Please enter your choice: ')
        if choice == '1':
            exchanger_currency()
        if choice == '2':
            show_currency()
        if choice == '3':
            show_gold()
        if choice == '4':
            exchanger_gold()
        if choice == 'e':
            print('See You')
            show_menu = False


menu()
