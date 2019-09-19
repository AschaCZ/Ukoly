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
#přidej nějaké formátování, aby to nevypadalo tak jednotvářně - nadpis u tahu i bonusu, odsazení (prázdný print)

import random
import time

# Losování pěti čísel v tahu
def losovani(tah):
	cislo = random.randint(1,100)
	los = f'Vylosováno bylo číslo {cislo}.'
	print(los)
	time.sleep(0.5)

# Losování bonusového tahu
def bonus():
	bonus = random.randint(1,100)
	if bonus == 11 or bonus == 22 or bonus == 33 or bonus == 44 or bonus == 55 or bonus == 66 or bonus == 77 or bonus == 88 or bonus == 99:
		vyhra = f'Vylosoval si bonusové číslo {bonus}! JACPOT!'
		print(vyhra)
	else:
		prohra = f'Vylosoval si bonusové číslo {bonus}! Bohužel vyhrávají zdvojená čísla, zkus to příště.'
		print(prohra)

def __main__():
	print('Vítejte při dnešním losování sportky. Jako každý den losujeme 2 tahy po pěti číslech a také Vás neochudíme o bonusový tah!')
	for tah in range(1,3):
		time.sleep(1)
		print(' ')
		print(f'******** {tah}. tah ********')
		print(' ')
		time.sleep(0.5)
		for i in range(1,6):
			losovani(tah)
	print(' ')
	print('******* Bonusový tah *******')
	print(' ')
	time.sleep(1.2)
	bonus()

__main__()