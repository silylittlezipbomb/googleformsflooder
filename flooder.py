import requests
import threading
import colorama
from colorama import *
import os
import random
import string

colorama.init(strip=False)

counter = 0 # don't change this, this just counts up

threadsamt = int(input("How many threads? (2 shouldn't rate limit but is slow): "))

url = input("Enter the url here (should have /formResponse at the end): ")

data = {}
valuesWithRand = []

if len(data) == 0:

    def get_data():
        key = input("key: ")
        value = input("value: ")
        useRand = input("add random characters to this value? (y/n): ")

        if useRand.lower() == "y":
            valuesWithRand.append(key)
        
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
        for x in valuesWithRand:
            randstring = (''.join(random.choices(string.ascii_letters, k=5)))
            data[x] = f"{data[x]} [{randstring}]"

        r = requests.post(url, data=data)

        for x in valuesWithRand:
            data[x] = data[x][:-8]

        if r.status_code == 200:
            global counter
            counter += 1
            print(Fore.GREEN + f"Successfully submitted! ({counter})")
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
