import requests
import json
url = ' http://saral.navgurukul.org/api/courses/74/exercises'
response = requests.get(url)             
k = json.loads(response.text)
print(k["data"]) 
j=int(input("enter one id number"))
for i in k["data"]:
    if str(j) in k["data"]:
        print(i["id"]["name"])
    break
