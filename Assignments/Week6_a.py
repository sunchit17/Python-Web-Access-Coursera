import urllib.parse, urllib.request, urllib.error
import json

url = input('Enter URL - ')
data = urllib.request.urlopen(url).read()

info = json.loads(data)

comments = info["comments"]
sum = 0

for comment in comments:
    sum+=comment["count"]

print(sum)    
