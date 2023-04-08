
import requests
# baseUrl='http://localhost:8004/api'
baseUrl='http://localhost:8003/api'
entityName='eyesightRes'
# path='EyesightResListGetCreateTime'
path='EyesightResListGetCreateTimeEyesightRes'


# http://localhost:8080/api/eyesightRes/save
# res=requests.post('http://43.142.150.223:8003/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
# res=requests.post('http://localhost:8004/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
# res=requests.post('http://localhost:8004/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
# EyesightResListGetCreateTime
# res=requests.post(f'{baseUrl}/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
# res=requests.post(f'{baseUrl}/{entityName}/{path}',data={})
# res=requests.post(f'{baseUrl}/{entityName}/{path}',data=[])
# res=requests.post(f'{baseUrl}/{entityName}/{path}',data=[1])
# Content type 'application/x-www-form-urlencoded;charset=UTF-8' not supported
# =requests.post json 
import json

# dic = {'key1': 'value1', 'key2': 'value2'}
dic = {
  "ids": []
}
# Content type 'application/octet-stream' not supported
string = json.dumps(dic)
# res=requests.post(f'{baseUrl}/{entityName}/{path}',data=string)
# headers = {'Content-Type': 'application/json'}
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

# 1.先导入库：
import datetime

# 2.获取当前日期和时间：
# now_time = datetime.datetime.now()

# ————————————————
# 版权声明：本文为CSDN博主「我是那颗银弹」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_40272386/article/details/105658398
# res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=string)
# res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=[])
url="http://43.142.150.223:8003/api/eyesightRes/save"
# url="http://localhost:8003/api/eyesightRes/save"

# ok 
now_time = datetime.datetime.now()

eyesightResToSave= {  
						  # "leftEyesight": None,
                            # "leftEyesight": 4.5,
#                             res
# <Response [502]>
  # "leftEyesight": "4.5",
  
  # res
# <Response [200]>
# {"code":1,"message":"成功","response":true}
 "leftEyesight": 4.5,
#  res
# <Response [200]>
# {"code":1,"message":"成功","response":true}
# res
# <Response [502]>
					
						     "userName":"starp" ,
							   "userCode":1 ,
							     "createTime":now_time,
                  #  python  现在时间 
                # 这些注释了就可以成功 难道是一个接口的数据太多了 这还多吗。/。
                # 不注释下面的话 失败的很多 7/10 吧  失败。的原因是 502
                	   "rightEyesight":None ,
				      
						
				         "createUserId":None ,
				         "departId":None ,
				         "departName":None ,
				         "deviceId":None ,
				         "deviceName":None ,
				         "enableMark":None ,
				         "id":None ,
				         "isDeleted":None ,
				     
				         "memo":None ,
				        
				         "testTime":None ,
				         "updateTime":None ,
				         "updateUserId":None ,
				       
				         "userId":None ,
				       
				         "userSex":None 
				                  }

import time

def save_one():
  # res=requests.post(url,headers=headers,json=eyesightResToSave)
  res=requests.post(url,headers=headers,json=eyesightResToSave)
  # python requests.post( 传递 springboot Date怎么传递呀 ?
  # 传递这个不行 now_time = datetime.datetime.now()
  # {"code":1,"message":"成功","response":true}

  # res=requests.post(url,headers=headers,data=eyesightResToSave)
  # =requests.post( 请求后端 json 
  # https://blog.csdn.net/qq_40272386/article/details/105658398
          
  # res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data={})
  # res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=dic)
  # requests.post header  json
  print("res")

  print(res)

  # {requests.post
  #   "ids": []
  # }
  print(res.text)
  time.sleep(0.1)
  # time.sleep(3)

  # Required request body is missing  requests.post
  # D:\proj\python\my_util_py_pub>python postman_test.py
  # {"code":500,"message":"系统内部错误","response":None}

  # res
  # <Response [200]>
  # {"code":1,"message":"成功","response":true}


for i in range(0,10):
  print(i)
  save_one()

"""
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [502]>

res
<Response [502]>

res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [502]>

res
<Response [502]>

res
<Response [502]>

res
<Response [502]>

res
<Response [502]>

res
<Response [502]>

"""

"""

D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\postman_test.py"
res
<Response [502]>

res
<Response [502]>

res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [502]>

"""

# 接口有时候成功有时候 502

"""

D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\postman_test.py"
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}
res
<Response [200]>
{"code":1,"message":"成功","response":true}

D:\proj\python\my_util_py_pub>
"""

"""
localhost  本地就可以

D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\postman_test.py"
0
res
<Response [200]>
{"code":1,"message":"成功","response":true}
1
res
<Response [200]>
{"code":1,"message":"成功","response":true}
2
res
<Response [200]>
{"code":1,"message":"成功","response":true}
3
res
<Response [200]>
{"code":1,"message":"成功","response":true}
4
res
<Response [200]>
{"code":1,"message":"成功","response":true}
5
res
<Response [200]>
{"code":1,"message":"成功","response":true}
6
res
<Response [200]>
{"code":1,"message":"成功","response":true}
7
res
<Response [200]>
{"code":1,"message":"成功","response":true}
8
res
<Response [200]>
{"code":1,"message":"成功","response":true}
9
res
<Response [200]>
{"code":1,"message":"成功","response":true}
"""