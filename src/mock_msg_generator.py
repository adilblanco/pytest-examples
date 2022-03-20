import random
from datetime import date


def get_today_name():
    return date.today().strftime('%A')


def get_message():
    return f'Hello {get_today_name()}!'


def get_code():
    rand_int = random.randint(0, 9)
    return f'CX-{rand_int}'

# def get_today_name():
#     return date.today().strftime('%a')


def get_code_with_day():
    code = get_code()
    dayname = get_today_name().upper()
    return f'{code}-{dayname}'
