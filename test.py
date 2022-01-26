import requests
from bs4 import BeautifulSoup


# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)

# open('facebook.ico', 'wb').write(r.content)

from pickle import load, dump

with open('filepage_list', 'rb') as pickle_Obj:
    filepage_list = load(pickle_Obj)

buffer_list = []
page_number = 1
for lateral in filepage_list:

    url = 'http://radiospecials.fusionbd.com/'+lateral

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    buffer = [i['href'] for i in soup.find_all('a', href=True)]

    for i in buffer:
        if i.__contains__('download.php'):
            buffer_list.append(i)
    print(page_number)
    page_number += 1

with open('finalfile', 'wb') as pickle_obj:
    dump(buffer_list, pickle_obj)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

print("!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!")