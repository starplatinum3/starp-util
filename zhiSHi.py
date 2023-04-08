import requests

url = "https://api.ownthink.com/kg/knowledge?entity=职业回答机器人"

response = requests.get(url)

data = response.json()
print("data")
print(data)

print(data['data']['avp'][0]['value'])