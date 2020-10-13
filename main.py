from constants import dollar_to_rial


def price_menu():
    show_menu = True
    while show_menu:

        user_input = int(input('how much dollar you have?\n enter 0 to quit\n'))

        if not user_input:
            show_menu = False

        result = dollar_to_rial(dollar = user_input)

        print(result)
        


price_menu()