#open file in a new terminal session> python consume.py
#to consume API (server of API must be running)

import requests

response = requests.get('http://127.0.0.1:8000/drinks')
print (response.json())