import requests

link="https://zajecia-programowania-xd.pl/kubus_puchatek"
kubus_raw = requests.get(link)

kubus_text = kubus_raw.text #.encode('utf-8'))

kubus_linie_b = kubus_text.split('</p>')
#print(kubus_text)


# czyszczenie
kubus_linie = []
for l in kubus_linie_b:
#	l = l[4:]
	l = l.replace('<p>', '')
	l = l.strip()

	kubus_linie.append(l)
#	print(l)

# wyswietlanie
licznik = 0
start = 100
end = 400

tajemniczy_bohater = 'Cyber marian'
bohater_2 = 'dot MS'
bohater_3 = 'Goku'
for index, linia in enumerate(kubus_linie):
	
	if index >= start and index < end:
		linia = linia.replace('Kubuś' , tajemniczy_bohater)
		linia = linia.replace('Puchatek' , tajemniczy_bohater)
		linia = linia.replace('Królik' ,  bohater_2 )
		linia = linia.replace('Prosiaczek' ,  bohater_3 )
		linia = '<p>' + linia + '</p>'
		print(linia)
print()
print('<p>Czytała Krystyna Cubówna</p>')
# linia.replace('Królik' ,  bohater_2 )
#		print(index,linia)
		

#	if  'Kubus' in linia:
#		print(index, linia)
#		licznik = licznik+1

print(len(kubus_linie))
print(licznik)

