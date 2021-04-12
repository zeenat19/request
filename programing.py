import requests
import json,pprint

url = 'http://saral.navgurukul.org/api/courses'
response = requests.get(url)             
data = json.loads(response.text)
pprint.pprint(data["availableCourses"])
# print(data)
j=int(input("enter a number"))

i=0
while i<len(data["availableCourses"]):
   if str(j) == (data["availableCourses"][i]["id"]):
      print(data["availableCourses"][i]["name"]) 
      break
   i=i+1
   