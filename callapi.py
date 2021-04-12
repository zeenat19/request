import requests
import json
import os 

baseUrl = "http://saral.navgurukul.org/api/courses"
print("****************************** welcome to saral *****************************")
# Checking if coures cache is there or not 
def checkCoursesCaching(url):
    if os.path.isfile('./courses.json'):
        file = open("courses.json")
        temp = file.read()
        data = json.loads(temp)
        file.close()
        return(data)

    # if json file dosn't exists then request data 
    else:
        request = requests.get("http://saral.navgurukul.org/api/courses")
        data = request.json()
        s = json.dumps(data,indent=4)# json. dumps() function converts a Python object into a json string.
        #indent 4 using because its look like a dictionary and key
        with open("courses.json", "w") as file:
            file.write(s)
            file.close()
            return(data)
# print(checkCoursesCaching(baseUrl))

# createing cache of selected exercise
print("*****its courses name*****")
def CreateExperciseCaching(coursesdata):
    list_of_id = []
    for i in range(len(coursesdata["availableCourses"])):
        print( i+1, coursesdata["availableCourses"][i]["name"]) 
        list_of_id.append(coursesdata["availableCourses"][i]["id"])
    choice=int(input("Which course you want to join  "))
    for i in range(len(list_of_id)):
        if (choice-1) == i:
            courseName = coursesdata['availableCourses'][i]["name"]
            # if individual course file exists then read the coursesdata
            if os.path.isfile("./exercises_"+courseName+".json"):
                file = open("exercises_"+courseName+".json")
                temp = file.read()
                subdata=json.loads(temp)
                file.close()
                return subdata
                # if individual course file edoesn't exists then request the url and a
            else:
                request1=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_of_id[i])+"/exercises")
                subdata=request1.json()
                s=json.dumps(subdata,indent=4)
                with open("exercises_"+courseName+".json", "w") as f:
                    f.write(s)
                    f.close()
                    return subdata

getCourseData = checkCoursesCaching(baseUrl)
# print(getCourseData)

selectedExercise = CreateExperciseCaching(getCourseData)
# print(selectedExercise)
print("************its parent****************** ")
def getSlugData(selectedExercise):
    courseName = selectedExercise["data"][0]["name"]
    parent = selectedExercise["data"]
    slugP = []
    for i in range(len(parent)):
        print (str(i+1),parent[i]["name"])
        slugP.append(parent[i]["slug"])
        for j in range(len(parent[i]['childExercises'])):
            print (parent[i]['childExercises'][j]["name"] )
            slugP.append(parent[i]['childExercises'][j]["slug"])
    print("***************child Exercise*******************")
    user_input=int(input(" slug you want to see  "))

    # print content of the slug
    for i in range(len(slugP)):
        if (user_input) == i:
            if os.path.exists("./exercise_"+courseName+str(user_input)+".json"):
                file = open("exercise_"+courseName+str(user_input)+".json")
                temp = file.read()
                slug_1 = json.loads(temp)
                file.close()
                print (slug_1["content"])
            else:
                request2 = requests.get("http://saral.navgurukul.org/api/courses/12/exercise/getBySlug?slug="+str(slugP[i]))
                sc = request2.json()
                p = json.dumps(sc,indent=4)#dumps() json. dumps() function converts a Python object into a json string. 
                with open("exercise_"+courseName+str(user_input)+".json", "w") as f:
                    f.write(p)
                    f.close()

                f = open("exercise_"+courseName+str(user_input)+".json")
                temp = f.read()
                slug_1 = json.loads(temp)#The json. loads() is used to convert the JSON String document into the Python dictionary.
                f.close()
                print (slug_1["content"])

getSlugData(selectedExercise)