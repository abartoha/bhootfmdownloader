from re import match
import requests
from bs4 import BeautifulSoup

from pickle import dump

url_list = []
url_page_list = ['index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=0&sort=0','index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=1&sort=0', 'index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=2&sort=0', 'index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=3&sort=0', 'index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=4&sort=0', 'index.php?dir=Bhoot_FM/High_Quality-MP3_Version&p=0&page=5&sort=0']

url = 'http://radiospecials.fusionbd.com/'
match_string = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Songket', 'Short', 'FM']

page_number = 1
for lateral in url_page_list:
    root_url = url+lateral
    buffer_url = ''
    buffer_list = []
    
    req = requests.get(root_url)

    soup = BeautifulSoup(req.content, 'html.parser')
    buffer = [i['href'] for i in soup.find_all('a', href=True)]

    for i in buffer:
        for j in match_string:
            if not buffer_url.__contains__(i):
                buffer_url += i
                buffer_url += 'CODENAME'
    #print("PAGE "+str(page_number))
    buffer_list = buffer_url.split('CODENAME')
    for i in buffer_list:
        if not url_list.__contains__(i):
            url_list.append(i)
    #print(buffer_list)
    page_number += 1

print('--------------------------------CHECK!-------------------------------------')

filepage_list = []
buffer_list = []
buffer_url = ''

# for i in match_string:
#     for j in url_list:
#         if j.__contains__(i):
#             print(j)
print('--------------------------------CHECK!-------------------------------------')
page_number = 1
for lateral in url_list:
    root_url = url+lateral
    req = requests.get(root_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    buffer = [i['href'] for i in soup.find_all('a', href=True)]
    for i in buffer:
        if i.__contains__('file.php'):
            if not buffer_list.__contains__(i):
                buffer_url += i
                buffer_url += 'CODENAME'
    buffer_list = buffer_url.split('CODENAME')
    for i in buffer_list:
        if not filepage_list.__contains__(i):
            filepage_list.append(i)
    print(page_number)
    page_number += 1

# with open('filepage_list', 'wb') as pickle_obj:
#     dump(filepage_list, pickle_obj)

# for lateral in filepage_list:
#     root_url = url+lateral
#     buffer_url = ''
#     buffer_list = []
#     req = requests.get(root_url)

#     soup = BeautifulSoup(req.content, 'html.parser')
#     buffer = [i['href'] for i in soup.find_all('a', href=True)]
#     for i in buffer:
#         if i.__contains__('mp3'):
#             if not buffer_list.__contains__(i):
#                 buffer_url += i
#                 buffer_url += 'CODENAME'
#     buffer_list = buffer_url.split('CODENAME')
#     for i in buffer_list:
#         if not filepage_list.__contains__(i):
#             filepage_list.append(i)
#     print(page_number)
#     page_number += 1

