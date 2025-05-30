import json , ssl
import urllib.request , urllib.parse 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serv = 'http://py4e-data.dr-chuck.net/opengeo/json?'
while True:
    ads = input('Enter the wanted url:')
    ads = ads.strip()
    pams = dict()
    pams['q'] = ads
    url = serv + urllib.parse.urlencode(pams)
    print('Retriving...' , url)
    uh = urllib.request.urlopen(url , context = ctx)
    data = uh.read().decode()
    print('Retrived:-' , len(data) ,' charcters'.replace('\n' , ' '))
    print("Raw data preview:\n", data[:300])
    try :
        js = json.loads(data)
    except:
        print('unable to find')
        break
    if not 'plus_code' in js :
        print('not found')
        break
    print(json.dumps(js, indent=2))