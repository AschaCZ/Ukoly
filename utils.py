#utils lib

import random
import time

#formátování názvu tahů
def format(text, sleep_time=1):

    time.sleep(sleep_time)
    print(f'\n******** {text} tah ********\n')
    time.sleep(sleep_time)

def random_number():
    number = random.randint(1,100)
    return number

def hello():
    print('Vítejte při dnešním losování sportky! \nJako každý den losujeme 2 tahy po pěti číslech a také Vás neochudíme o bonusový tah!')

bonus = False