import requests


request = requests.get("https://api.npoint.io/ed99320662742443cc5b")
request.raise_for_status
data_2 = request.json()
print( data_2[0]['title'])