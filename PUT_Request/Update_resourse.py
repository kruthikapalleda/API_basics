import requests
import json
import jsonpath


# API Url
url = "https://reqres.in/api/users/2"

#Read input JSON file
file = open('./Updated_userdata.json','r')
json_input = file.read()

#parse the data into json format
request_json = json.loads(json_input)
#print(request_json)

#Make PUT_Request with json input body
response_put = requests.put(url,request_json)
#print(response_post.content)

#validating the response status code
assert response_put.status_code == 200

#Parse response content
response_json = json.loads(response_put.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])






