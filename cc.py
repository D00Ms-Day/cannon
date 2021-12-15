#!/usr/bin/env python3
import time
import os
import sys
from pyfiglet import Figlet
from colorama import Fore

def slowprint(n):
    for word in n + '\n':
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.10)
def banner():
    os.system("clear")
    custom_fig = Figlet(font='times')
    print(custom_fig.renderText('CC VALIDATOR'))
    slowprint(Fore.YELLOW+"""                        <<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>
                        <<<<<<<<<<<<<<<->>>>>>>>>>version 1.0
                        ----============================-----
                        |+|   DEVELOPER : D00MS D4Y       |+|
                        |+|   TEAM : ANONYMOUS ELITES     |+|
                        |+|   FACEBOOK : ANONYMOUS ELITES |+|
                        ----============================-----
                        <<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>>>>
                        <<<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>""")

banner()
print()

def slowprint(n):
    for word in n + '\n':
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.10)
def __start__():
    card_number = list(input(Fore.WHITE+"[+] Enter Card Number: ").strip())
    check_digit = card_number.pop()
    card_number.reverse()
    processed_digits = []

    for index, digit in enumerate(card_number):
        if index % 2 == 0:
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:
                doubled_digit - 9
                processed_digits.append(doubled_digit)
    else:
        processed_digits.append(int(digit))
        total = int(check_digit) + sum(processed_digits)

    if total % 10 == 0:
            print(Fore.GREEN+"[+] Wahoo! It's A Valid Card!")
    else:
        print(Fore.RED+"[-] Oops It's An Invalid Card!")
__start__()
