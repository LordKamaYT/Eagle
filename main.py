from pystyle import *
import hashlib
import os
from getpass import getpass
import requests
import subprocess

banner = '''
__________                 .__           
\_   _____/_____      ____  |  |    ____  
 |    __)_ \__  \    / ___\ |  |  _/ __ \ 
 |        \ / __ \_ / /_/  >|  |__\  ___/ 
/_______  /(____  / \___  / |____/ \___  >
        \/      \/ /_____/             \/ '''[1:]
banner1 = '''
__________                 .__           
\_   _____/_____      ____  |  |    ____  
 |    __)_ \__  \    / ___\ |  |  _/ __ \ 
 |        \ / __ \_ / /_/  >|  |__\  ___/ 
/_______  /(____  / \___  / |____/ \___  >
        \/      \/ /_____/             \/


          Press Enter...'''[1:]


def intro():
    Anime.Fade(text=Center.Center(banner1),
               color=Colors.red_to_blue,
               mode=Colorate.Horizontal,
               enter=True,
               time=True,
               interval=0.5)
    print(Colorate.Horizontal(Colors.red_to_blue, banner, 1))
    print(Box.DoubleCube("Hello, Welcome to Eagle."))


def license():
    # Make pastebin with keys and just get the raw
    keys = requests.get("https://pastebin.com/raw/M39BY5Jq").text
    # License key from user.
    keyfromuser = input("Enter license key:  ")
    for key in keys.splitlines():
        if key == keyfromuser:
            print('Login successful !')
            return
        print('Wrong key')


def actionLogin():
    actionLoginKey = ''
    while actionLoginKey == "":
        os.system('clear')
        print(Colorate.Horizontal(Colors.blue_to_green, banner, 1))
        print()
        actionLoginAsk = '''What action do you want to perform ?
          [1] - Get key
          [2] - Enter key
          [3] - Key not working ?
          [4] - Arzerox-Spammer
          [5] - Exit'''
        print(Colorate.Horizontal(Colors.blue_to_green, actionLoginAsk, 1))
        actionLoginKey = Write.Input(f"Enter Choice: ",
                                     Colors.blue_to_green,
                                     interval=0.05)
    if actionLoginKey == '2':
        license()
    if actionLoginKey == '4':
        subprocess.call([r'./arzerox-start.bat'])


intro()
actionLogin()
