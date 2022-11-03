import requests
import json

API_KEY = 7e4e35be8cde79d957b79bcba094bdb7
LAT = -7.11532
LOG = -34.861
url = (f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta = requests.request("GET", url)
objetos = json.loads(resposta.txt)
#dados- objetos = dados

for i in objetos:
    print(f"{i} ::{objetos[i]}")
