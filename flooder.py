import requests
import threading
import colorama
from colorama import *
import os

colorama.init(strip=False)

counter = 0 # don't change this, this just counts up

threadsamt = int(input("threads (2 shouldn't rate limit but is slow): "))

url = input("enter the url here (should have /formResponse at the end): ")

data = {}

if len(data) == 0:

    def get_data():
        key = input("key: ")
        value = input("value: ")
        data[key] = value

    get_data()

    while True:
        answer = input("add more? (y/n): ")
        if answer.lower() == "y":
            get_data()
        elif answer.lower() == "n":
            break
        else:
            print("invalid response")

os.system('cls')

def submit():
    while True:
        r = requests.post(url, data=data)
        if r.status_code == 200:
            global counter
            counter += 1
            print(Fore.LIGHTGREEN + f"Successfully submitted! ({counter})")
        elif r.status_code == 429:
            print(Fore.YELLOW + f"Rate limited!")
        else:
            print(Fore.RED + f"Failed to submit! Error code: {r.status_code}")

threads = []

for i in range(threadsamt):
    t = threading.Thread(target=submit)
    threads.append(t)

for i in range(threadsamt):
    threads[i].start()

for i in range(threadsamt):
    threads[i].join()
