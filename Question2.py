import requests
import json
        

api = "https://reqres.in/api/users?page="
userCount = 0
pageCount = 1 
isData = True
while isData == True:
    responce = requests.get(api+str(pageCount))
    datas = json.dumps(responce.json(), indent = 4)
    dict1 = {}
    dict1 =json.loads(datas)
    cnt=len(dict1['data'])
    if cnt>0:
        userCount = userCount + cnt
        pageCount=pageCount+1
    else:
        isData = False

print("Total users : " + str(userCount))
