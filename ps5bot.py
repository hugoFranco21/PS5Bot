from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
from datetime import datetime
import os
import json
import time

def check_availability(url, name, message, driver, client):
    driver.get(url)
    el = driver.find_element_by_tag_name('body')
    if(el.text.find(message) != -1):
        print('Shit boiii')
        return True
    else:
        send_message(name, client, url)
        return False

def send_message(name, client, url):
    mensaje = 'This is not a drill, hay PS5 en ' + name + ' ' + url
    message = client.messages \
                .create(
                    body=mensaje,
                    from_='+19737379720',
                    to='+5215554024649'
                )

# path to chromedriver.exe 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGFILE = os.environ.get("TWILIO_CREDENTIALS", f"{BASE_DIR}/ps5bot/TWILIO_CREDENTIALS.json")
with open(CONFIGFILE) as config_file:
    config = json.load(config_file)


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
path = '/usr/bin/chromedriver'
# create nstance of webdriver
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
# google url
url = ['https://www.amazon.com.mx/Consola-PlayStation-5-Standard-Edition/dp/B08H6SBB2R/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91',
        'https://www.sams.com.mx/search/Ntt=consola-ps5',
        'https://www.costco.com.mx/Electronicos/Videojuegos/PlayStation/Playstation-5-Consola/p/662351',
        'https://www.coppel.com/consola-playstation-5-de-825-gb-pm-2893773',
        'https://store.sony.com.mx/PlayStation5/p',
        'https://www.bestbuy.com.mx/p/sony-consola-playstation-5-blanco/1000232279',
        'https://www.sanborns.com.mx/producto/149872/consola-playstation-5/',
        'https://gameplanet.com/consola-playstation-5.html']

account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

while True:
    if not check_availability(url[0],
        'Amazon',
        'No disponible por el momento.',
        driver,
        client):
        break
    if not check_availability(url[1],
        'Sam\'s',
        'No Disponible',
        driver,
        client):
        break
    if not check_availability(url[2],
        'Costco',
        'Agotado',
        driver,
        client):
        break
    if not check_availability(url[3],
        'Coppel',
        'Producto no disponible',
        driver,
        client):
        break
    if not check_availability(url[4],
        'Sony',
        'Producto sin stock',
        driver,
        client):
        break
    if not check_availability(url[5],
        'Best Buy',
        'Agotado',
        driver,
        client):
        break
    if not check_availability(url[6],
        'Sanborns',
        'Producto no disponible',
        driver,
        client):
        break
    if not check_availability(url[7],
        'Game Planet',
        'Por el momento este producto no se encuentra disponible',
        driver,
        client):
        break
    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(120)
