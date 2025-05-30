import json , ssl
import urllib .request , urllib.parse
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = 'http://py4e-data.dr-chuck.net/opengeo'
adess = input('Enter the location:-')
adess = adess.strip()
parms = dict()
parms ['q'] = adess
url = link + '?' + urllib.parse.urlencode(parms)
#url = link + urllib.parse.urlencode(parms)
print('Rentriving...' , url)
stiff = urllib.request.urlopen(url , context=ctx)
data = stiff.read().decode()
print('Retrived:-' , len(data) , 'Charcters')
js = json.loads(data)
print(json.dumps(js, indent=4))
# type , features , plus_code ,FeatureCollection ,Feature,
print('pluss code' , js['features'][0]['properties']['plus_code'])