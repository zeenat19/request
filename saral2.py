import requests
import json

url = ' http://saral.navgurukul.org/api/courses'
response = requests.get(url)           
k = json.loads(response.text)
for i in k["availableCourses"]:
    print(i["name"])