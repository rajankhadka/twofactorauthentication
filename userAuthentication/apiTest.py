import requests
import json

data = {
    'username': 'newUser5',
    'password': 'rajan9848041474',
    'email': 'email@email.com',
    'phoneNumber': 9848286722
}


logindata = {
    'username': 'newUser5',
    'password': 'rajan9848041474',
}

json_data = json.dumps(data)

data1 = {
    'username': 'newUser5',
    'otp': 563823
}


requests.post('http://127.0.0.1:8000/user/login/', data=json.dumps(logindata))

# requests.post('http://127.0.0.1:8000/user/otpcode/', data=json.dumps(data1))
