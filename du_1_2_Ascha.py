# vytvorit program kde:
			# definuji 2 funkce
			# pouziji cyklus
			# pouziji if
			# 
# loterie
# 
# 1) import random
# 2) losovani 5 cisel (1-100)
# 3) 2 tahy
# 4) vyuzit if - bonus
# přidej nějaké formátování, aby to nevypadalo tak jednotvářně - nadpis u tahu i bonusu, odsazení (prázdný print)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

def format(text, sleep_time=1):

	time.sleep(sleep_time)
	print(f'\n******** {text} tah ********\n')
	time.sleep(sleep_time)

# Náhodné číslo

def random_number():
	number = random.randint(1,100)
	
	return number

# Losování pěti čísel v tahu

def losovani():

	cislo = random_number()
	print(f'Vylosováno bylo číslo {cislo}.')
	time.sleep(0.5)

'''
# Vybrání bonusu z vylosovaných čísel - nefunguje

def bonus_cislo():
	win = [11, 22, 33, 44, 55, 66, 77, 88, 99]
	if random_number() in win:
		print(f'Mezi vylosovanými je dvojité číslo. Vyhráváš JACPOT!')
	else:
		print(f'Bohužel, mezi vylosovanými čísly není dvojité číslo. Snad přístě.')

# Losování bonusového tahu - funkční

def bonus():
	bonus = random.randint(1,100)
	if bonus == 11 or bonus == 22 or bonus == 33 or bonus == 44 or bonus == 55 or bonus == 66 or bonus == 77 or bonus == 88 or bonus == 99:
		vyhra = f'Vylosoval si bonusové číslo {bonus}! JACPOT!'
		print(vyhra)
	else:
		prohra = f'Vylosoval si bonusové číslo {bonus}! Bohužel vyhrávají zdvojená čísla, zkus to příště.'
		print(prohra)
'''

# Odhad uživatele
def odhad():

	odhad = int(input('Vložte Váš odhad bonusového čísla: '))

	print('...')
	time.sleep(0.5)
	print('...')
	time.sleep(0.5)
	
	return odhad

# porovnání	
def user_bonus():

	bonus = random_number()

	if odhad() == random_number():
		print(f'Správně jsi odhal bonusové číslo {bonus}, gratuluji!')

	else:
		print(f'Bohužel, bylo vylosováno číslo {bonus}. Snad příště.')


def __main__():

	print('Vítejte při dnešním losování sportky. Jako každý den losujeme 2 tahy po pěti číslech a také Vás neochudíme o bonusový tah!')
	
	for tah in range(1,3):
		format(f'{tah}.', 1)

		for i in range(1,6):
			losovani()

	format('Bonusový', 1.5)

	user_bonus()
	#bonus_cislo()
	#bonus()

__main__()