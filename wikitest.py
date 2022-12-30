import requests
import os
import wikipedia
import random
from lxml import html

def create_folders():
	try:
		os.mkdir("static/hero_image")
	except:
		pass
	try:
		os.mkdir("static/flag_image")
	except:
		pass
	try:
		os.mkdir("saved_heroes")
	except:
		pass
	try:
		os.mkdir("hero_think")
	except:
		pass

def gather_heroes():

	heroes = [
		'Tadeusz Kościuszko',
		#'Władysław Sikorski',
		#  'Witold Pilecki',
		# 'Maria Skłodowska-Curie',
		# 'Józef Haller',
		# 'Wojciech Korfanty',
	]

	greetings = [
		'pozdrawia',
		'/wave',
		'/wink',
		'wita',
	]

	wikipedia.set_lang("pl")

	saved_heroes = os.listdir('saved_heroes')
	saved_heroes = [h.split('.')[0] for h in saved_heroes]

	for hero in heroes:
		hero_think(hero)
		# podzielić bit/flaga zmiany poprzez # <h2><span 
		# wykycie <h2><span id="O_
		if True :#hero not in saved_heroes:

			# Get some info and link.
			some_info = wikipedia.page(hero)
			# print(some_info.content)
			# print(type(some_info))
			info_intro = some_info.content.split('\n\n')[0] 
			url = '<a href="'+some_info.url+'">Poszukaj więcej info o: '+hero+"</a>"
			
			
			# Get what hero thinks.
			# hero_think(hero)
			
			# Get & save images.
			images = some_info.images
			n_photos = 0
			for i, image_url in enumerate(images):
				if i < 3:
					hero_str = '11'.join(hero.split())
					image_name = '{}_{}.legend'.format(hero_str, i)

					n_photos += 1
			# print(hero + '\n')
			# print(str(n_photos) + '\n')
			# print(info_intro + '\n')
			# print(url)

			# Save all.
			# with open('saved_heroes/'+hero+".hero", "w+") as f:
				# f.write(hero + '\n')
				# f.write(str(n_photos) + '\n')
				# f.write(info_intro + '\n')
				# f.write(url)

	


		else:
			greeting = random.choice(greetings)
			print(hero, greeting)

def hero_think(name):
	url_name = name.replace(' ', '_')
	url = 'https://pl.wikiquote.org/wiki/{}'.format(url_name)
	hero_wikiquotes = requests.get(url)
	print(hero_wikiquotes.text)
	cudze_cytaty = False
	#with open('hero_think/'+name+".hero", "w+") as f:
	with open('dtxt/'+name+"cyt.hero", "w+") as f:
		for line in hero_wikiquotes.text.split('\n'):
		# podzielić bit/flaga zmiany poprzez # <h2><span 
		# wykycie <h2><span id="O_
			if line.startswith('<h2>O'):
				continue
			if line.startswith('<h2><span id="O_'):
				cudze_cytaty = True
				continue
			
			if ((cudze_cytaty == True) and (line.startswith('<h2><span'))):
				cudze_cytaty = False
			if cudze_cytaty == True :
				continue
			
			if line.startswith('<ul><li>'):
				tree = html.fromstring(line)
				quote = tree.text_content().strip()
				if not quote.startswith('Opis') and not quote.startswith('Autor') and not quote.startswith('Źródło') and not quote.startswith('Zobacz te'):
					f.write(quote + '\n')
			# 		q = Quotes(
			# 			person_id=person_id, 
			# 			quote=quote,
			# 		)
			# 		db.session.add(q)
			# 		db.session.commit()


create_folders()
gather_heroes()