import os
import time
import requests
from colorama import Fore, Style

def read_webhooks():
    try:
        with open("webhooks.txt", "r") as webhookfile:
            return webhookfile.readlines()
    except FileNotFoundError:
        print(Fore.RED + "Error: 'webhooks.txt' file not found.")
        return []

def nuke(webhook, message):
    nukedata = {'content': message}
    response = requests.post(webhook, json=nukedata)
    if response.status_code == 200:
        print(Fore.GREEN + f"Message sent to {webhook}")
    else:
        print(Fore.RED + f"Failed to send message to {webhook}, Status Code: {response.status_code}")

def main():
    webs = read_webhooks()
    webcount = len(webs)
    
    if webcount == 0:
        print(Fore.RED + "No webhooks found. Exiting.")
        return

    message = ""
    main_title = f"""{Fore.RED}
         ,-.--,               .-._                     ,--.-.,-.      ,----.               
.--.-.  /=/, .',--.-.  .-,--./==/ \  .-._ .--.-. .-.-./==/- |\  \  ,-.--` , \  .-.,.---.   
\==\ -\/=/- / /==/- / /=/_ / |==|, \/ /, /==/ -|/=/  ||==|_ `/_ / |==|-  _.-` /==/  `   \   | Webhooks: {webcount} |
 \==\ `-' ,/  \==\, \/=/. /  |==|-  \|  ||==| ,||=| -||==| ,   /  |==|   `.-.|==|-, .=., |  | Made by sudzythegoat |
  |==|,  - |   \==\  \/ -/   |==| ,  | -||==|- | =/  ||==|-  .|  /==/_ ,    /|==|   '='  /  
 /==/   ,   \   |==|  ,_/    |==| -   _ ||==|,  \/ - ||==| _ , \ |==|    .-' |==|- ,   .'  
/==/, .--, - \  \==\-, /     |==|  /\ , ||==|-   ,   //==/  '\  ||==|_  ,`-._|==|_  . ,'.  
\==\- \/=/ , /  /==/._/      /==/, | |- |/==/ , _  .' \==\ /\=\.'/==/ ,     //==/  /\ ,  ) 
 `--`-'  `--`   `--`-`       `--`./  `--``--`..---'    `--`      `--`-----`` `--`-`--`--'  
"""
    choices = """
[1] Nuke
[2] Set Message
[3] Update URLS
"""
    print(main_title)
    print(choices)
    
    while True:
        options = input("[>] ")
        if options == "1":
            if not message:
                print(Fore.YELLOW + "Please set a message")
            else:
                for webhook in webs:
                    nuke(webhook.strip(), message)
        elif options == "2":
            message = input("Set nuke message\n[>] ")
        elif options == "3":
            os.system("cls" if os.name == 'nt' else 'clear')
            time.sleep(0.5)
            webs = read_webhooks()
            webcount = len(webs)
        else:
            print(Fore.RED + "Invalid")
if __name__ == "__main__":
    main()
