#ip and phone checker by VolodyaHoi
#vk.com/vl.hoi0
#t.me/vl_hoi1

#libs

from pif import get_public_ip
import urllib.request
from urllib.request import urlopen
import json
from json import load
import os
import colorama
from colorama import Fore, Back, Style

def LogoType(): #logotype loading
    print(Fore.WHITE + '''
    ██╗░░░░░░█████╗░''' + Fore.RED + '''██╗''' + Fore.WHITE + '''░░░''' + Fore.RED + '''██╗''' + Fore.WHITE + '''███████╗██████╗░
    ██║░░░░░██╔══██╗''' + Fore.RED + '''██║''' + Fore.WHITE + '''░░░''' + Fore.RED + '''██║''' + Fore.WHITE + '''██╔════╝██╔══██╗
    ██║░░░░░██║░░██║''' + Fore.RED + '''╚██╗''' + Fore.WHITE + '''░''' + Fore.RED + '''██╔╝''' + Fore.WHITE + '''█████╗░░██████╔╝
    ██║░░░░░██║░░██║░''' + Fore.RED + '''╚████╔╝''' + Fore.WHITE + '''░██╔══╝░░██╔══██╗
    ███████╗╚█████╔╝░░''' + Fore.RED + '''╚██╔╝''' + Fore.WHITE + '''░░███████╗██║░░██║
    ╚══════╝░╚════╝░░░░''' + Fore.RED + '''╚═╝''' + Fore.WHITE + '''░░░╚══════╝╚═╝░░╚═╝\n''' + Fore.WHITE + "-" * 60 + Fore.YELLOW + "\nIP and Phone Number checker by VolodyaHoi\nYour IP Adress: "+ get_public_ip() + "\n" + Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    print("[" + Fore.RED + "1" + Style.RESET_ALL + "] Check IP Adress")
    print("[" + Fore.RED + "2" + Style.RESET_ALL + "] Check Phone Number")
    print("[" + Fore.RED + "3" + Style.RESET_ALL + "] Exit")

    print(Fore.CYAN + "=" * 60)

def clear(): #clear logs
    os.system('cls' if os.name == 'nt' else 'clear')

def start(): #start checker

    CMD = int(input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter Command: "))

    if CMD == 1: #ip checker
        getIP = input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter IP Address: ")
        url = "https://ipinfo.io/" + getIP + "/json"
        try:
            url = "https://ipinfo.io/" + getIP + "/json"
            getInfo = urllib.request.urlopen(url)
            infoList = json.load(getInfo)

            print(Fore.CYAN + "-" * 60)
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " IP: ", infoList["ip"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " City: ", infoList["city"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Region: ", infoList["region"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Country: ", infoList["country"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Location: ", infoList["loc"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Organisation: ", infoList["org"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Postal: ", infoList["postal"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Timezone: ", infoList["timezone"])
            print(Fore.CYAN + "-" * 60)
            next = input(Fore.GREEN + "Press ENTER to go back...")
            back()

        except: #error
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid IP Address!")
            next = input(Fore.GREEN + "Press ENTER to go back...")
            back()

    elif CMD == 2: #phone number checker

        phoneNumber = input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter phone number: ")

        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phoneNumber

        try:
            infoPhone = urllib.request.urlopen(getInfo)

            infoPhone = json.load(infoPhone)

            print(Fore.CYAN + "-" * 60)
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Phone Number: ", "+" + phoneNumber)
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Country: ", infoPhone["country"]["english"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Region: ", infoPhone["region"]["english"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " District: ", infoPhone["region"]["okrug"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " AutoCod: ", infoPhone["region"]["autocod"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Location: ", infoPhone["0"]["latitude"], infoPhone["0"]["longitude"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Operator: ", infoPhone["0"]["oper"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Timezone: ", infoPhone["0"]["tz"])
            print(Fore.CYAN + "-" * 60)

            next = input(Fore.GREEN + "Press ENTER to go back...")
            back()
        except: #error
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid phone number!")
            next = input(Fore.GREEN + "Press ENTER to go back...")
            back()

    elif CMD == 3: #exit =)

        exit()

    else: #error

        print(Fore.RED + "[!]" + Style.RESET_ALL + " Wrong command number!")
        next = input(Fore.GREEN + "Press ENTER to go back...")
        back()

def back(): #go back
    clear()
    LogoType()
    start()

#first start
clear()
LogoType()
start()

