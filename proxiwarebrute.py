import requests, os, threading, gratient
from threading import active_count, Thread
from colorama import Fore

port = 1999
country = input("Enter a country Code \nE.x: us\n-> ")
base = "proxiware.com"

print("推奨Threadは1です、それ以外の場合はportが重複する恐れがあります。")

def brute():
    global port, country, base
    port += 1
    os.system(f"title Infinity Proxy is Now Working. Checking for - {country}.{base}:{port}")
    Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
    req = requests.get(f'https://hypixel.net/', headers=Header, proxies=dict(http=f"http://{country}.{base}:{port}", https=f"http://{country}.{base}:{port}"))
    if req.status_code == 200:
        aaa = gratient.purple("Alive Proxy")
        print(f"{aaa} ->{Fore.RESET} {country}.{base}:{port}")
        f = open('aliveproxies.txt', 'a', encoding='UTF-8')
        f.write(f'{country}.{base}:{port}\n')
        f.close()
    elif req.status_code == 403:
        aaa = gratient.purple("Alive Proxy, but Forbidden")
        print(f"{aaa} ->{Fore.RESET} {country}.{base}:{port}")
        f = open('Forbidden.txt', 'a', encoding='UTF-8')
        f.write(f'{country}.{base}:{port}\n')
        f.close()
    elif req.status_code == 429:
        aaa = gratient.purple("Alive Proxy, but RateLimited.")
        print(f"{aaa} ->{Fore.RESET} {country}.{base}:{port}")
        f = open('RateLimited.txt', 'a', encoding='UTF-8')
        f.write(f'{country}.{base}:{port}\n')
        f.close()
    else:
        aaa = gratient.yellow(f"{country}.{base}:{port}is Not Working\nStatus Code -> {req.status_code}")
        print(aaa)

if __name__ == "__main__":
    NThread = input("何threadにする?  -> ")
    while True:
        Run = True
        while Run:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except:
                    pass
    else:
            if active_count() <= int(NThread):
                try:
                    Thread(target=brute).start()
                except Exception as e:
                    print("error")
