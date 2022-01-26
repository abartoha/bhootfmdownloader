import requests
from bs4 import BeautifulSoup

url = 'http://radiospecials.fusionbd.com/index.php?dir=Bhoot_FM/High_Quality-MP3_Version/April_2012&p=0&sort=0'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

buffer = [i['href'] for i in soup.find_all('a', href=True)]

for i in buffer:
    if i.__contains__('file.php'):
        print(i)