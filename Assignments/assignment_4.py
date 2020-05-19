import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL - ')
retrieved  =  urllib.request.urlopen(url).read()

tree = ET.fromstring(retrieved)
counts = tree.findall('.//count')

sum = 0

for count in counts:
    value = int(count.text)
    sum+=value

print(sum)
