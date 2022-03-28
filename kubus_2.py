import requests

link="https://zajecia-programowania-xd.pl/kubus_puchatek"
kubus_raw = requests.get(link)

kubus_text = kubus_raw.text #.encode('utf-8'))
kubus_text = kubus_text.replace('</p>', '')
kubus_text = kubus_text.replace('<p>', '')

ileznakow = len(kubus_text)
print(ileznakow)

kubus_puchatek_slowa = kubus_text.split()
kubus_puchatek_slowa_n = len(kubus_puchatek_slowa) 

print(kubus_puchatek_slowa_n)

