import requests
import json


data = {
    'id': 5,
    'name': 'raj',
    'age': 230,
    'address': 'npj',
}

parse_data = json.dumps(data)

# r = requests.get('http://localhost:8001/student/3/')
# print(r.json())
requests.delete('http://localhost:8001/student/delete/', data=parse_data)
