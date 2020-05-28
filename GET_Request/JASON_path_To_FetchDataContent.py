import requests
import json
import jsonpath

#API Url

url = "https://reqres.in/api/users?page=2"

#Send Get request

response = requests.get(url)


#Parse the response to JSON format

json_response = json.loads(response.text)
#print(json_response)

#Fetch value by using JSON path

pages = jsonpath.jsonpath(json_response,'total_pages')
assert  pages[0] == 2
#print(pages[0])


