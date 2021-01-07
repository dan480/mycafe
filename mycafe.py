# -*- coding: utf-8 -*-
# using Python 3

"""
@ MyCafe
@repository github.com/dan480/mycafe
@author dan480
@about: The program is a simulator of ordering in a cafe.
@description: The program shows how decorators work.
              Passing an argument to a decorator is shown.
              The logic for accepting an order,
              processing an order and exiting an order is implemented.
"""


# block decorator
def coffee(func):
    """
    The decorator that adds coffee
    """
    def wrapper():
        print('=--------=')
        print('= coffee =')
        func()
    return wrapper


def water(func):
    """
    The decorator that adds water
    """
    def wrapper():
        print('=--------=')
        print('= water  =')
        func()
    return wrapper


def milk(func):
    """
    The decorator that adds milk
    """
    def wrapper():
        print('=--------=')
        print('=  milk  =')
        func()
    return wrapper


def ice_cream(func):
    """
    The decorator that adds ice_cream
    """
    def wrapper():
        print('=--------=')
        print('=ice_cream')
        func()
    return wrapper


def whipped_milk(func):
    """
    The decorator that adds whipped_milk
    """
    def wrapper():
        print('=--------=')
        print('= whipped=')
        print('=  milk  =')
        func()
    return wrapper


def grated_chocolate(func):
    """
    The decorator that adds grated_chocolate
    """
    def wrapper():
        print('=........=')
        print('=grated  =')
        print('=chocolate')
        print('=........=')
        func()
    return wrapper


def chocolate(func):
    """
    The decorator that adds chocolate
    """
    def wrapper():
        print('=++++++++=')
        print('=chocolate')
        func()
    return wrapper


def sugar(sugar_arg):
    """
    The decorator with argument that adds sugar
    """
    def wrapper(func):
        def called():
            print(sugar_arg)
            func()
        return called

    return wrapper


# block func
@coffee
def espresso():
    """
    The function that creates espresso
    """
    cup()


@coffee
@sugar('=..sugar.=')
def espresso_sugar():
    """
    The function that creates espresso
    """
    cup()


@water
@coffee
def americano():
    """
    The function that creates americano
    """
    cup()


@water
@coffee
@sugar('=..sugar.=')
def americano_sugar():
    """
    The function that creates americano
    """
    cup()


@whipped_milk
@milk
@coffee
def cappuccino():
    """
    The function that creates cappuccino
    """
    cup()


@whipped_milk
@milk
@coffee
@sugar('=..sugar.=')
def cappuccino_sugar():
    """
    The function that creates cappuccino
    """
    cup()


@whipped_milk
@coffee
def macchiato():
    """
    The function that creates macchiato
    """
    cup()


@whipped_milk
@coffee
@sugar('=..sugar.=')
def macchiato_sugar():
    """
    The function that creates macchiato
    """
    cup()


@grated_chocolate
@ice_cream
@coffee
def glace():
    """
    The function that creates glace
    """
    cup()


@grated_chocolate
@ice_cream
@coffee
@sugar('=..sugar.=')
def glace_sugar():
    """
    The function that creates glace
    """
    cup()


@whipped_milk
@coffee
@chocolate
def marocchino():
    """
    The function that creates marocchino
    """
    cup()


@whipped_milk
@coffee
@chocolate
@sugar('=..sugar.=')
def marocchino_sugar():
    """
    The function that creates marocchino
    """
    cup()


def cup():
    """
    A function that draws the cup
    """
    print('==========')
    print(' =======\n')


def a_else():
    """
    A function that draws the cup
    """
    # Asks the user what he wants else
    order = input('Anything else? \n'
                  'If "no", the program will end.\n').lower()
    # Asking the user if he wants sugar
    if order != 'no':
        sugar = input('Would you like some sugar in your coffee?\n').lower()
    else:
        sugar = ''
    return order, sugar


def wish():
    """
    The function that writes "goodbye"
    """
    print('\n')
    print('====================================')
    print('   You are welcome.                 ')
    print('           Have a nice day!         ')
    print('====================================')


# body program
if __name__ == '__main__':
    print('=========================================')
    print('=         TODAY IN OUR CAFE             =')
    print('=                                       =')
    print('=     1. Espresso      (E)              =')
    print('=     2. Americano     (A)              =')
    print('=     3. Cappuccino    (C)              =')
    print('=     4. Marocchino    (M)              =')
    print('=     5. Glace         (G)              =')
    print('=     6. Macchiato     (MA)             =')
    print('=                                       =')
    print('=    All coffee is free today           =')
    print('= =======================================')
    print('\n')
    try:
        # Asks the user what he wants
        order = input('Hi! Would you like something to drink? \n'
                      '''Write the number, first letter
                      or name of the coffee.\n''').lower()
        # Asks the user if he wants sugar
        sugar = input('Would you like some sugar in your coffee?\n').lower()
        # Cycle that processes the order
        while True:
            if order in ['espresso', '1', 'e']:
                if sugar == 'yes':
                    espresso_sugar()
                else:
                    espresso()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order in ['americano', '2', 'a']:
                if sugar == 'yes':
                    americano_sugar()
                else:
                    americano()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order in ['cappuccino', '3', 'c']:
                if sugar == 'yes':
                    cappuccino_sugar()
                else:
                    cappuccino()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order in ['marocchino', '4', 'm']:
                if sugar == 'yes':
                    marocchino_sugar()
                else:
                    marocchino()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order in ['glace', '5', 'g']:
                if sugar == 'yes':
                    glace_sugar()
                else:
                    glace()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order in ['macchiato', '6', 'ma']:
                if sugar == 'yes':
                    macchiato_sugar()
                else:
                    macchiato()
                order, sugar = a_else()
                if order == 'no':
                    break
            if order not in ['1', '2', '3', '4', '5', '6',
                             'e', 'a', 'c', 'm', 'g', 'ma',
                             'espresso', 'americano',
                             'cappuccion', 'marocchino',
                             'glace', 'macchiato']:
                print('Sorry, I don\'t understand you. \n')
                order = a_else()
                if order == 'no':
                    break
    finally:
        wish() # Exit from the program, words of gratitude.
