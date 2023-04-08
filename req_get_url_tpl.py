
# //    http://localhost:8889/acc/last
# url='http://localhost:8889/acc/last'
base_url='http://localhost:8003'
url=f'{base_url}{methodURL}'

# url='http://localhost:8003/api/all/getAllURL'
import requests
res=requests.post(url, data={'url':'http://localhost:8889/acc/last'})
# res=requests.get(url)
print(res.text)

