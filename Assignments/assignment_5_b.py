import urllib.parse, urllib.request, urllib.error
import json

queryurl='http://py4e-data.dr-chuck.net/json?'
api_key = input('Enter API Key - ')
inp_address = input('Enter Address - ')

if(len(inp_address)<1):
    print('Insufficient Info')

else:
    parms = dict()
    parms['key'] = api_key
    parms['address'] = inp_address
    url = queryurl+urllib.parse.urlencode(parms)
    data = urllib.request.urlopen(url).read()
    try:
        info = json.loads(data)
    except:
        info = None
    if not info or 'status' not in info or info['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)

    place_id = info['results'][0]['place_id']
    print(place_id)
