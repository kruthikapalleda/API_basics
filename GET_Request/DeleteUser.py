import requests

#API Url

url = "https://reqres.in/api/users/2"

#Delete

response = requests.delete(url)

#Fetch response code

#print(response.status_code)

assert response.status_code == 204
