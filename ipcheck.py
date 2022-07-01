# IP and phone checker by VolodyaHoi
# vk.com/vl.hoi0
# t.me/vl_hoi1

# Code review by cd-con and eel-primo
from pif import get_public_ip
from urllib.request import urlopen
from json import load
import os
from colorama import Fore, Back, Style
import sys

def header(): # Header
    print(Fore.WHITE + '''
    ██╗░░░░░░█████╗░''' + Fore.RED + '''██╗''' + Fore.WHITE + '''░░░''' + Fore.RED + '''██╗''' + Fore.WHITE + '''███████╗██████╗░
    ██║░░░░░██╔══██╗''' + Fore.RED + '''██║''' + Fore.WHITE + '''░░░''' + Fore.RED + '''██║''' + Fore.WHITE + '''██╔════╝██╔══██╗
    ██║░░░░░██║░░██║''' + Fore.RED + '''╚██╗''' + Fore.WHITE + '''░''' + Fore.RED + '''██╔╝''' + Fore.WHITE + '''█████╗░░██████╔╝
    ██║░░░░░██║░░██║░''' + Fore.RED + '''╚████╔╝''' + Fore.WHITE + '''░██╔══╝░░██╔══██╗
    ███████╗╚█████╔╝░░''' + Fore.RED + '''╚██╔╝''' + Fore.WHITE + '''░░███████╗██║░░██║
    ╚══════╝░╚════╝░░░░''' + Fore.RED + '''╚═╝''' + Fore.WHITE + '''░░░╚══════╝╚═╝░░╚═╝\n''' + Fore.WHITE + "-" * 60 + Fore.YELLOW 
          + "\nIP and Phone Number checker by VolodyaHoi\nYour IP Adress: "+ get_public_ip() + "\n" + Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    print("[" + Fore.RED + "1" + Style.RESET_ALL + "] Check IP Adress")
    print("[" + Fore.RED + "2" + Style.RESET_ALL + "] Check Phone Number")
    print("[" + Fore.RED + "3" + Style.RESET_ALL + "] Exit")
    print(Fore.CYAN + "=" * 60)

def clear(): # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def procced_command(): # Proceed user input
    CMD = input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter Command: ")

    if CMD == '1': # IP checker
        try:
            getIP = input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter IP Address: ")
            url = "https://ipinfo.io/" + getIP + "/json"
            
            getInfo = urlopen(url)
            infoList = load(getInfo)

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
            
            _ = input(Fore.GREEN + "Press ENTER to go back...")
            
            run()
        
        # Too broad!
        except:
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid IP Address!")
            _ = input(Fore.GREEN + "Press ENTER to go back...")
            run()

    elif CMD == '2': # Phone number checker
        phoneNumber = input(Fore.YELLOW + "[" + Fore.BLUE + ">" + Fore.YELLOW + "]" + Style.RESET_ALL + " Enter phone number: ")
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phoneNumber

        try:
            infoPhone = urlopen(getInfo)
            infoPhone = load(infoPhone)

            print(Fore.CYAN + "-" * 60)
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Phone Number: ", "+" + phoneNumber)
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Country: ", infoPhone["country"]["english"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Region: ", infoPhone["region"]["english"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " District: ", infoPhone["region"]["okrug"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " AutoCod: ", infoPhone["region"]["autocod"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Location: ", infoPhone["0"]["latitude"], 
                                                                                                            infoPhone["0"]["longitude"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Operator: ", infoPhone["0"]["oper"])
            print(Fore.YELLOW + "[" + Fore.BLUE + "+" + Fore.YELLOW + "]" + Style.RESET_ALL + " Timezone: ", infoPhone["0"]["tz"])
            print(Fore.CYAN + "-" * 60)

            _ = input(Fore.GREEN + "Press ENTER to go back...")
            run()
            
        # Too broad!
        except:
            print(Fore.RED + "[!]" + Style.RESET_ALL + " Invalid phone number!")
            next = input(Fore.GREEN + "Press ENTER to go back...")
            run()

    elif CMD == '3': # Stop the script
        sys.exit()

    else: # Incorrect input
        print(Fore.RED + "[!]" + Style.RESET_ALL + " Wrong command number!")
        _ = input(Fore.GREEN + "Press ENTER to go back...")
        run()

def run():
    clear()
    header()
    proceed_command()
    
# TODO implement OOP
if __name__ == "__main__":
    run()
