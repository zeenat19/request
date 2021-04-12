import requests
import json

url = ' https://saral.navgurukul.org/api/courses'
response = requests.get(url)          
k = json.loads(response.text)
print(k)