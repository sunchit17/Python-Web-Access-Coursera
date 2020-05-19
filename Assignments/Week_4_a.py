import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url  = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
count = 0
for tag in tags:
    count+=int(tag.contents[0])

print(count)
