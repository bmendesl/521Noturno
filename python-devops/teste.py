#!/home/developer/521Noturno/python-devops/venvaula1/bin/python3

import requests

data = requests.get('http://127.0.0.1:5000/joao')

print(data.json())