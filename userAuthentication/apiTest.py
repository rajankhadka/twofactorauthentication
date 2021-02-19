import requests
import json

data = {
    'username': 'newUser52',
    'password': 'rajan9848041474',
    'email': 'email@email.com',
    'phoneNumber': 9848286722
}

json_data = json.dumps(data)

requests.post('http://127.0.0.1:8000/user/login/', data=json_data)
