import requests, os, threading, gratient, random
from threading import active_count, Thread
from colorama import Fore

base = "44.208.236.109:31112"

def brute():
    global base
    Test = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    s = ''.join(random.choice(Test) for _ in range(7))
    session = f"orpbjyow:4KtJuPRrkNgC3Jpi_session-{s}"
    os.system(f"title Infinity Proxy is Now Working. Checking for - {session}@{base}")
    Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
    req = requests.get(f'https://hypixel.net/', headers=Header, proxies=dict(http=f"http://{session}@{base}", https=f"http://{session}@{base}"))
    if req.status_code == 200:
        aaa = gratient.purple("Alive Proxy")
        print(f"{aaa} ->{Fore.RESET} {session}@{base}")
        f = open('aliveproxies.txt', 'a', encoding='UTF-8')
        f.write(f'{session}@{base}\n')
        f.close()
    elif req.status_code == 403:
        aaa = gratient.purple("Alive Proxy, but Forbidden")
        print(f"{aaa} ->{Fore.RESET} {session}@{base}")
        f = open('Forbidden.txt', 'a', encoding='UTF-8')
        f.write(f'{session}@{base}\n')
        f.close()
    elif req.status_code == 429:
        aaa = gratient.purple("Alive Proxy, but RateLimited.")
        print(f"{aaa} ->{Fore.RESET} {session}@{base}")
        f = open('RateLimited.txt', 'a', encoding='UTF-8')
        f.write(f'{session}@{base}\n')
        f.close()
    else:
        aaa = gratient.yellow(f"{session}@{base} is Not Working\nStatus Code -> {req.status_code}")
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
