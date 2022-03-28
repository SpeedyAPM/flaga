import configparser
import os

config = configparser.ConfigParser()
config.read('settings.ini')

domena = config['XD']['domena']

# 1. Usun pliki konfiguracji serwera nginx
nginx_1 = '/etc/nginx/sites-available/{}'.format(domena)
nginx_2 = '/etc/nginx/sites-enabled/{}'.format(domena)

# 2. Usun pliki plik gunicorna
guni = '/etc/systemd/system/flaga.service'

for f in [guni, nginx_1, nginx_2]:
        print('Removing ', f)
        os.system('rm {}'.format(f))

