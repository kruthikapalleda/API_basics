import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

#ValidTE sTATUS cODE
assert response.status_code == 200

#Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#Fetch Cookies
print(response.cookies)
#Fetch Encoding
print(response.encoding)

print(response.elapsed)