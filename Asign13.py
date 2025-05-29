import json
import urllib.request , urllib.parse
url ='http://py4e-data.dr-chuck.net/comments_42.json'
data = urllib.request.urlopen(url).read()
stuff = json.loads(data)
print('Retriving..' , len(data) , 'charcters')
total = 0 
num =0
counts = stuff['comments']
for item in counts:
    total += int(item['count'])
    num += 1
print('Sum' , total)
print('counts' , num)