from constants import dollar_to_toman


def price_menu():
    show_menu = True
    while show_menu:

        number_of_dollars = int(input('how much dollar you have?\n enter 0 to quit\n'))

        if not number_of_dollars:
            show_menu = False


        result = dollar_to_toman(dollar = number_of_dollars)

        print(f"{number_of_dollars} dollar = {result} toman")
        
price_menu()