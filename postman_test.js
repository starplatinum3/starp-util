
// import requests
// # baseUrl='http://localhost:8004/api'
baseUrl='http://localhost:8003/api'
entityName='eyesightRes'
// # path='EyesightResListGetCreateTime'
path='EyesightResListGetCreateTimeEyesightRes'

// fetch()

// Example POST method implementation:
async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

postData('https://example.com/answer', { answer: 42 })
  .then(data => {
    console.log(data); // JSON data parsed by `data.json()` call
  });

  postData(`${baseUrl}/${entityName}/${path}`, { answer: 42 })
  .then(data => {
    console.log(data); // JSON data parsed by `data.json()` call
  });



// # http://localhost:8080/api/eyesightRes/save
// # res=requests.post('http://43.142.150.223:8003/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
// # res=requests.post('http://localhost:8004/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
// # res=requests.post('http://localhost:8004/api/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
// # EyesightResListGetCreateTime
// # res=requests.post(f'{baseUrl}/userEventLog/save',data={'user_id':1,'event_type':'back_dir_log','event_data':'{"from_path":"from_path","to_path":"to_path"}'})
// # res=requests.post(f'{baseUrl}/{entityName}/{path}',data={})
// # res=requests.post(f'{baseUrl}/{entityName}/{path}',data=[])
// # res=requests.post(f'{baseUrl}/{entityName}/{path}',data=[1])
// # Content type 'application/x-www-form-urlencoded;charset=UTF-8' not supported
// # =requests.post json 
// import json

// # dic = {'key1': 'value1', 'key2': 'value2'}
// dic = {
//   "ids": []
// }
// # Content type 'application/octet-stream' not supported
// string = json.dumps(dic)
// # res=requests.post(f'{baseUrl}/{entityName}/{path}',data=string)
// headers = {'Content-Type': 'application/json'}
// // # res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=string)
// // # res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=[])
// res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data={})

// # res=requests.post(f'{baseUrl}/{entityName}/{path}',headers=headers,data=dic)
// # requests.post header  json


// # {requests.post
// #   "ids": []
// # }
// print(res.text)

// # Required request body is missing  requests.post
// # D:\proj\python\my_util_py_pub>python postman_test.py
// # {"code":500,"message":"系统内部错误","response":null}