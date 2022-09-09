import requests, os, threading, gratient
from threading import active_count, Thread
from colorama import Fore

type = input("input Proxy Type Here\n-> ")
proxy = input("input Proxy Here\n-> ")

def brute():
    global proxy, type
    ip = requests.get("https://api.ipify.org", proxies=dict(http="{type}://{proxy}", https="{type}://{proxy}")).text
    print(gratient.purple(f"Proxie's ip == {ip}"))

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
