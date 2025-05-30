import json
import urllib.request , urllib.parse
adress = input('Enter the name of the location:-')
param = urllib.parse.urlencode({'q': adress , 'format' : 'json'})
url =f'https://nominatim.openstreetmap.org/search?{param}'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url , headers = headers)
res = urllib.request.urlopen(req)
data = json.loads(res.read())
if data:
    print('LONGIE' , data[0]['lon'])
    print('LATHIE' , data[0]['lat'])
else : print('locaion not found')