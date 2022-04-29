from flask import Flask, render_template
import os
import random
import re

from moje_programy.character_wiki import character
from moje_programy.character_wiki import character2
from moje_programy.open_poem import open_poem

app=Flask(__name__)

if __name__=="__main__":
	
	app.run()

how_many = 3


@app.route('/ciekawe-postacie')
def ciekawe_postacie():
#	asa
	lista_ciekawych_postaci = [
		'Małysz',
		'Kopernik',
		'Maria Skłodowska',
		'Kościuszko',
		'Donald',
		'Myszka Miki'
	]
	opisy_postaci  = []
	for i in range(how_many):
		postac = random.choice(lista_ciekawych_postaci)
		indeks = lista_ciekawych_postaci.index(postac)
		lista_ciekawych_postaci.pop(indeks)
		opis_postaci = character(postac)
		dlugos_opisu = len(opis_postaci)
		ilosc_slow = len(re.findall(r'\w+', opis_postaci))
		info = [postac, opis_postaci, dlugos_opisu , ilosc_slow ]
		opisy_postaci.append(info)
	opisy_postaci.sort( key = lambda x: x[3] , reverse=True  )#chooseWordsCount) #ilosc_slow:ilosc_slow[how_many]
#	ciekawa_postac =  character( random.choice(lista_ciekawych_postaci))
	return render_template("ciekawe-postacie.html" ,   opisy_postaci =opisy_postaci)

@app.route('/brudnopis')
def brudnopis():
#	superhero = character("Ija Kiwa")
	super_heroes = ['Bruce Lee' ,'Tygrysek' , 'Kłapouchy' , 'Kopernik']
	chosen_hero = random.choice( super_heroes).encode('utf-8').decode()
	kangur = character( chosen_hero)
	return render_template("brudnopis.html", hero2 = super_heroes, hero3 = kangur, super_heroes=super_heroes)


@app.route('/')
def index():
	text2 =  open('xd.txt').read()
	text= "siema tu łłłźźżżż  XDD" + text2 + "HAHA  " + text2
	return render_template("index.html", text=text)

@app.route('/kubus_puchatek')
def kubus_puchatek():

	return render_template("kubus_puchatek.html")



@app.route('/xd')
def xd():
	return render_template("xd.html")

if __name__=="__main__":
	app.run()

@app.route('/zpxd')
def zpxd():
	return "ZPXD"

@app.route('/siema-cyryl')
def siema_cyryl():
	return render_template("Siema Cyryl.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
	poem_lines = open_poem()
	return render_template("flaga-dla-ukrainy.html", poem = poem_lines)
