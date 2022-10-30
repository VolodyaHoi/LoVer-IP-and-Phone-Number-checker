# IP and phone checker by VolodyaHoi
# vk.com/id631406971
# t.me/atomthreatsup

# Code review by cd-con

from pif import get_public_ip
import urllib.request
from urllib.request import urlopen
import json
from json import load
import os
import colorama
from colorama import Fore, Back, Style

def header(): # Header
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

def clear(): # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def procced_command(): # Proceed user input
    CMD = int(input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter Command: "))

    if CMD == 1: # IP checker
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
            
            main()
        
        # Too broad!
        except:
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid IP Address!")
            next = input(Fore.GREEN + "Press ENTER to go back...")
            main()

    elif CMD == 2: # Phone number checker
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
            main()
            
        # Too broad!
        except:
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid phone number!")
            next = input(Fore.GREEN + "Press ENTER to go back...")
            main()

    elif CMD == 3: # Stop the script
        exit()

    else: # Incorrect input
        print(Fore.RED + "[!]" + Style.RESET_ALL + " Wrong command number!")
        next = input(Fore.GREEN + "Press ENTER to go back...")
        main()

def main():
    clear()
    header()
    procced_command()

main()
# TODO implement OOP
