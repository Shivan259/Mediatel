import requests
from main import serverport, serveradress

res = requests.get("http://" + str(serveradress) + ":" + str(serverport) + "/api/2003")
res = requests.post("http://" + str(serveradress) + ":" + str(serverport) + "/api/2003", {"contact_id": 2001})

print(res.json())
