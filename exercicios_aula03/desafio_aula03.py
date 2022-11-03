import requests
import json

API_KEY= '7e4e35be8cde79d957b79bcba094bdb7'
LAT = 7.4361
LOG = 34.9128
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta = requests.request("GET", url)
objetos = json.loads(resposta.text)

for i in objetos:
    print(f'{i} :: {objetos[i]}')