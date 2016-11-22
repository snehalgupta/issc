from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

url = 'http://127.0.0.1:8000/localmin/done/3' # Set destination URL here
file = open('test.txt', 'r')
a = file.read()
print(str(file),a)
post_fields = {'file': a }     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)

#r = requests.post(url, files={'test.txt': open('test.txt', 'rb')})
#print(r.text)