import requests

#API Url
url = "https://reqres.in/api/users?page=2"

#Send Get request
response = requests.get(url)
#print(response)

#Display response content
print(response.content)
print(response.headers)
