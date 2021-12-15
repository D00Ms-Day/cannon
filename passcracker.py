#!/usr/bin/python3
import time
import hashlib
from colorama import Fore
from pyfiglet import Figlet
import os
import sys

def slowprint(n):
    for word in n + '\n':
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.11)
def banner():
    os.system("clear")
    custom_fig = Figlet(font='times')
    print(custom_fig.renderText('MD5 CR4CK3R'))
    slowprint(Fore.WHITE+"""                        <<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>
                        <<<<<<<<<<<<<<<->>>>>>>>>>version 1.0
                        ----============================-----
                        |+|   DEVELOPER : D00MS D4Y       |+|
                        |+|   TEAM : ANONYMOUS ELITES     |+|
                        |+|   FACEBOOK : ANONYMOUS ELITES |+|
                        ----============================-----
                        <<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>>>>
                        <<<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>""")

print()
banner()
flag = 0
counter = 0

pass_hash = input(Fore.LIGHTBLUE_EX+"[!] Enter MD5 Hash: ")
print()
wordlist = input(Fore.WHITE+"[!] Wordlist: ")
try:
    pass_file = open(wordlist, "r")
except:
    print(Fore.LIGHTRED_EX+"[x] Sorry No such file found!")
    quit()
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(Fore.YELLOW+"[!] Trying: " + pass_hash)
    counter += 1

    if digest == pass_hash:
        print(Fore.LIGHTYELLOW_EX+"[*] Password Found")
        print(Fore.LIGHTGREEN_EX+"[+] Password is " + word)
        print(counter)
        flag =1 
        break
if flag == 0:
    print(Fore.MAGENTA+"[!] Password Not Found In This List. Try Another!")

