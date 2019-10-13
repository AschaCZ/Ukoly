#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Losování dvou tahů o pěti číslech
# Jak na bonus z vylosovaných čísel? --> z listu?

#importy#
import random
import time

from utils import format, random_number, hello, bonus

#input, ošetření vstupu#
def user_input(message):
    while True:
        try:
            user_number = int(input(message))

        except ValueError: #když nastane chyba, print hlášky

            print("Tohle není správné číslo, zkus to ještě jednou!")
            continue

        else:

            if user_number <= 100 and user_number >= 1: #pouze čísla od 1 - 100

                return user_number
                break

            else:
                print("Tohle není správné číslo, zkus to ještě jednou!")

#losování#
def draw():

    number_list = []

    for a in range(1,6):
        number_list.append(random_number()) #tvorba listu o 5 číslech

    #print(number_list)
    return number_list


def bonus_draw():
    if bonus == True:
        print("\nTvoje číslo je mezi vylosovanými! Gratuluji k dobrému odhadu.")

    else:
        print("\nBohužel, tvůj odhad nebyl správný, zkus to příště!")


def __main__():

    hello()
    
    user_number = user_input("Tak jaké číslo mezi 1 a 100 si myslíš že dneska vylosujeme?  ")

    #print(user_number)    

    for tah in range(1,3):
       
        format(f'{tah}.', 1)
        number_list = draw()

        if user_number in number_list:
            bonus == True
   
        for n in range(0,5):
            print("Bylo vylosováno číslo " + str(number_list[n]) + "!")
            time.sleep(0.5)

    bonus_draw()


__main__()