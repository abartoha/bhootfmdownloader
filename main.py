import requests
from bs4 import BeautifulSoup
from pickle import dump, load
import datetime
from rich import print
now = datetime.datetime.now()
with open('error_log.txt', 'r') as error_log:
    if error_log.read() != '':
        print('Error Log Empty\n')

def error_log(string:str):
    with open('error_log.txt', 'a') as file:
        file.write(string)
        file.write('\n')

url = 'http://radiospecials.fusionbd.com/'

with open('finalfile', 'rb') as pickle_Obj:
    download_list = load(pickle_Obj)

download_number = 0
for i in download_list:
    download_start = datetime.datetime.now()
    root_url = url+i
    filename = i.split('/')[-1]
    print(download_start.strftime('%H:%M:%S, %d %B %Y')+' -> [yellow]Starting Download[/] ')
    error_log(download_start.strftime('%H:%M:%S, %d %B %Y')+' -> Starting Download ')
    try:
        download = requests.get(root_url, allow_redirects = True)
        download_end = datetime.datetime.now()
        print(download_end.strftime('%H:%M:%S, %d %B %Y')+' -> [green]Download Finished![/] ')
        error_log(download_end.strftime('%H:%M:%S, %d %B %Y')+' -> Download Finished! ')
    except:
        download_end = datetime.datetime.now()
        print(download_end.strftime('%H:%M:%S, %d %B %Y')+ ' -> [red]Download Failed![/] ')
        error_log(download_end.strftime('%H:%M:%S, %d %B %Y')+ ' -> Download Failed! ')

    try:
        open(filename,'wb').write(download.content)
        filemaking = datetime.datetime.now()
        print(filemaking.strftime('%H:%M:%S, %d %B %Y')+ ' -> [green]Filemade successfully[/] ')
        error_log(filemaking.strftime('%H:%M:%S, %d %B %Y')+ ' ->  Filemade successfully')

    except:
        filemaking = datetime.datetime.now()
        print(filemaking.strftime('%H:%M:%S, %d %B %Y')+ ' -> [bold red]Filemaking Failed[/] ')
        error_log(filemaking.strftime('%H:%M:%S, %d %B %Y')+ ' -> Filemaking Failed')
    download_number += 1

