
# //    http://localhost:8889/acc/last
# url='http://localhost:8889/acc/last'
base_url='http://localhost:8003'
url=f'{base_url}/api/all/getAllURL'

# url='http://localhost:8003/api/all/getAllURL'
import requests
res=requests.post(url, data={'url':'http://localhost:8889/acc/last'})
# res=requests.get(url)
print(res.text)

with open('req_get_url_py_req.py_res.json', 'w') as f:
    f.write(res.text)