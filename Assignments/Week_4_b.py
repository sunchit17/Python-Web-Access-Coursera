import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL : ')
count = input('Enter Count : ')
count = int(count)
position = input('Enter Position : ')
position = int(position)

for iterations in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href')


name = tags[position-1].contents[0]
print(name)
