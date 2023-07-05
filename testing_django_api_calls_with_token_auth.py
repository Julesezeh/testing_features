import requests
import json

url = "http://127.0.0.1:8000/api/v1"
headers = {
    "Authorization": "Token 0393ba2c87134934f579a38d9f50231957c69f82",
    "Content-Type": "application/json",
}

response = requests.get(url=url, headers=headers)
print(type(response.json()))
print((response.json()))
