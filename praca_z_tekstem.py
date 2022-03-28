import requests
import random

link="https://zajecia-programowania-xd.pl/kubus_puchatek"
kubus_raw = requests.get(link)

kubus_text = kubus_raw.text #.encode('utf-8'))

#x = "abc"  # str ("string")
#y = 1 #int (integer)

x =  "str ing"
print(link)
print(link.upper())
print(link.lower())
print(random.choice(x.split()))
