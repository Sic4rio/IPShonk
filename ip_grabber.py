import os
import socket
from colorama import Fore, Back, init as colorama_init
from termcolor import colored

colorama_init(autoreset=True)

def getIP(site):
    site = site.strip()
    try:
        if 'http://' not in site:
            IP1 = socket.gethostbyname(site)
            print(Fore.GREEN + "[+]" + Fore.WHITE + "IP: " + Fore.GREEN + IP1)
            with open('ips.txt', 'a') as f:
                f.write(IP1 + '\n')
    except Exception:
        print(Fore.RED + "[-]" + Fore.WHITE + "DOMAIN: " + Fore.RED + site)
        pass

def exit_gracefully():
    print('\n\n\t\t[-] Happy Hacking!...')
    os._exit(0)

def print_banner():
    banner = '''
    \t=======================================================================
    \t\t\t SICARIOS IP Grabber v1 - 2023
    \t=======================================================================
    '''
    print(Fore.YELLOW + banner + Fore.RESET)

if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()

        list_file = input((Fore.GREEN + Back.MAGENTA + '[+] Enter the file name containing URLs: ') + Fore.RESET)

        with open(list_file, 'r') as file:
            urls = file.readlines()

        total_sites = len(urls)
        index = 0

        for url in urls:
            index += 1
            print(Fore.GREEN + f"\n[+] Retrieving IP for {url.strip()} ({index}/{total_sites})")
            getIP(url)

        print(Fore.GREEN + "\n[+] IP addresses retrieved successfully and saved to ips.txt")
    except KeyboardInterrupt:
        exit_gracefully()
