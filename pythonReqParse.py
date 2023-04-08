
import json_util

# json_util. 

with open('req_get_url_py_req.py_res.json', 'r') as f:
    res=f.read()

json_obj=json_util.str_to_json_obj(res)

for req in json_obj:
    req:dict
    # print(req)
    pythonReq=req.get('pythonReq')
    # pythonReq=req['pythonReq']
    print(pythonReq)
