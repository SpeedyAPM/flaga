from flask import Flask, render_template, redirect, url_for

# Libraries

import random
import os
import wikipedia
import requests
from lxml import html

# FLASK

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

from moje_programy.character_wiki import character
from moje_programy.character_wiki import character2
from moje_programy.open_poem import open_poem
from moje_programy.open_data import open_data



app = Flask(__name__)
app.secret_key = ':)'

# Main

@app.route('/')
def index():
	print(dir(app))
	data_lines = open_data()
	return render_template("index.html", text=data_lines)

@app.route('/form_a', methods=["GET", "POST"])
def form_a():
    form = X()
    if form.validate_on_submit():
        x = form.x.data
        y = form.y.data
        z = form.z.data
        string = '{}\n{}\n{}\n\n'.format(x, y, z)
        save_data(string)
        return redirect( url_for('index'))
    return render_template("form_a.html", form=form)

@app.route('/form_b', methods=["GET", "POST"])
def form_b():
    form = MusicForm()
    if form.validate_on_submit():
        x = form.x.data
        z = form.z.data
        if z == True:
            string = '{}\n'.format(x)
            save_data(string)
            return redirect( url_for('index'))
        else:
            return render_template("form_b.html", form=form)
    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")



# Errors

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500

@app.route('/xd')
def xd():
	return render_template("xd.html")


# Form

class X(FlaskForm):
    x_options = [
            ('a','a'),
            ('b','b'),
            ('c','c'),
            ('d','d'),
            ('e','e'),
    ]
    x = StringField('x', validators=[DataRequired()])
    y = SelectField('y', choices=x_options)
    z = BooleanField('z')
    button = SubmitField('kk')

class MusicForm(FlaskForm):
    x = StringField('x', validators=[DataRequired()])
    z = BooleanField('z')
    button = SubmitField('kk')


# Helpers

# def save_data(string):
#     with open('data/data.txt', "a") as f:
#         f.write(string)


app.config['UPLOAD_FOLDER'] = 'static'


# Route

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
	# skłodowska i pilecki do poprawy opis, a razem conajmniej 5 bohaterów


@app.route('/flaga', methods=["GET", "POST"])
def flagapl():
	create_folders()

	# Flag.
	xd = random.choice(range(22))
	if len(os.listdir('static')) < 10:
		xd = 11
	flaga = os.path.join(app.config['UPLOAD_FOLDER'], 'Polska_Flaga__{}'.format(xd))
	
	# Gather heroes.
	heroes = gather_heroes()
	random.shuffle(heroes)

	return render_template("flaga.html", xd=xd, flaga=flaga, heroes=heroes)

def gather_heroes():
	
	heroes = [
		'Mikołaj Kopernik',
		'Józef Haller',
		'Władysław Sikorski',
#		'Witold Pilecki',
		'Rotmistrz Pilecki',
#		'Maria Skłodowska-Curie',
		'Maria Skłodowska',
		'Fryderyk Chopin',
 		'Kościuszko',
 		'Jan Henryk Dąbrowski',
 		'Wojciech Korfanty',
  		'Adam Mickiewicz',

	]
	# heroes = [
	# 	'Władysław Sikorski',
	# 	'Witold Pilecki',
	# 	'Maria Skłodowska-Curie',
	# 	'Józef Haller',
	# 	'Wojciech Korfanty',
	# ]

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
		if hero not in saved_heroes:

			# Get some info and link.
			some_info = wikipedia.page(hero)
			info_intro = some_info.content.split('==')[0]
			while info_intro[-1] is "\n":
				info_intro=info_intro[:-2]
			#### [0] - na końcu oznacza wziecie pierwszegi członu po zrobieniu splita(czyli wywalenie wszystkiego co jest po '\n\n')
			url = '<a href="'+some_info.url+'">Poszukaj więcej info o: '+hero+"</a>"
			
			
			# Get what hero thinks.
			hero_think(hero)
			
			# Get & save images.
			images = some_info.images
			n_photos = 0
			for i, image_url in enumerate(images):
				if i < 3:
					hero_str = '11'.join(hero.split())
					image_name = '{}_{}.legend'.format(hero_str, i)
					save_image(image_url, image_name)
					n_photos += 1

			# Save all.
			with open('saved_heroes/'+hero+".hero", "w+") as f:
				f.write(hero + '\n')
				f.write(str(n_photos) + '\n')
				f.write(info_intro + '\n')
				f.write(url)

		else:
			greeting = random.choice(greetings)
			print(hero, greeting)

	heroes = []
	for hero_file in os.listdir('saved_heroes'):
		hero = {}
		some_info = open('saved_heroes/'+hero_file).readlines()
		hero['name'] = some_info[0]
		photo_nr = random.choice(range(int(some_info[1])))
		hero_str = '11'.join(hero['name'][:-1].split())
		hero['image'] = '{}_{}.legend'.format(hero_str, photo_nr)
		hero_quotes = open('hero_think/' + hero['name'][:-1] + ".hero").readlines()
		hero['quote'] = random.choice(hero_quotes)
		hero['description'] = '\n'.join(some_info[2:-1])
		hero['description'] = bold(hero['description'])
		hero['url'] = some_info[-1]
		heroes.append(hero)
	return heroes

def save_image(image_url, image_name):
	image = requests.get(image_url).content
	save_as = 'static/hero_image/{}'.format(image_name)
	with open(save_as, 'wb') as ap:
		ap.write(image)
	return save_as

def bold(hero_info):

	nice = [
		'nauk',
		'gen',
		'zwy',
		'odk',
		'zał',
		'rod',
		'organizator',
		'astronom',
		'inżynier',
		'herbu',
		'wojska',
		'uczona',
		'nobla',
		'wybitniej',
		'romantyczny',
		'fizyk',
		'filozof',
		'kocha',
		'woli',
		'kawalerii',
		'skazany',
	]

	right_desc = []
	words = [w.lower() for w in hero_info.split()]
	for w in words:
		for woah in nice:
			if w.startswith(woah):
				w = '<b>'+w+'</b>'
		right_desc.append(w)
	right_desc = " ".join(right_desc)
	return right_desc

def hero_think(name):
	url_name = name.replace(' ', '_')
	url = 'https://pl.wikiquote.org/wiki/{}'.format(url_name)
	hero_wikiquotes = requests.get(url)
	with open('hero_think/'+name+".hero", "w+") as f:
		for line in hero_wikiquotes.text.split('\n'):
			if line.startswith('<h2>O'):
				continue
			if line.startswith('<ul><li>'):
				tree = html.fromstring(line)
				quote = tree.text_content().strip()
				if not quote.startswith('Opis') and not quote.startswith('Autor') and not quote.startswith('Źródło'):
					f.write(quote + '\n')


    # wojtekb@ip-172-31-29-234:/$ cp -r /home/wojtekb/zajecia_programowania_xd/3_tbd/028 /var/www/flaga
    # wojtekb@ip-172-31-29-234:/$ cp -r /home/wojtekb/zajecia_programowania_xd/3_tbd /var/www/flaga/zp028


# Folders


if __name__=="__main__":
    app.run(debug=True)