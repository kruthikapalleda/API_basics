import requests
import json
import jsonpath


# API Url
url = "https://reqres.in/api/users"


def test_create_new_user():
  #Read input JSON file
  file = open('./new_user.json','r')
  json_input = file.read()
  #parse the data into json format
  request_json = json.loads(json_input)
  #print(request_json)
  #Make POST_Request with json input body
  response_post = requests.post(url,request_json)
  #print(response_post.content)
  #validating the response status code
  assert response_post.status_code == 201
  #Fetch header from response ie.,response_post
  print(response_post.headers.get('Content-Length'))
  #parse response into json format
  response_json = json.loads(response_post.text)
  #pick id using json path
  id = jsonpath.jsonpath(response_json,'id')
  print(id[0])




