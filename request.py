import requests

url = 'http://localhost:5000/api'


r = requests.post(url, json={'wine_id': 3})

print(r.json())
