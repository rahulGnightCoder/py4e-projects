import json
import urllib.request , urllib.parse
url = input('Enter the url link:')
data = urllib.request.urlopen(url).read()
stuff = json.loads(data)
print('Retiving...' , len(stuff))
counts = stuff['comments']
total = 0 
num = 0 
for item in counts:
    total += int(item['count'])
    num += 1
print('Sum' , total)
print('count' , num)