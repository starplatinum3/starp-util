import json
import requests
import pandas as pd

# 获取tenant_access_token
# url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
# D:\proj\private-conf\feiShuApp.json
import json_util
post_data =json_util.file_path_to_dict(rf"D:\proj\private-conf\feiShuApp.json")
feiShuAccessToken =json_util.file_path_to_dict(rf"D:\proj\private-conf\feiShuAccessToken.json")
tenant_access_token=feiShuAccessToken["tenant_access_token"] 
tat=tenant_access_token
# tat=None
if tat is None:
    # 获取tenant_access_token
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    # post_data = {"app_id":"xxx",
    #              "app_secret":"xxx"}
    r = requests.post(url, data=post_data)
    tat = r.json()["tenant_access_token"]
    # D:\proj\private-conf\feiShuAccessTokenjson
    # D:\proj\private-conf\feiShuAccessTokenjson
    # D:\proj\private-conf\feiShuAccessToken
    # print('tat')
    # print(tat)
    feiShuAccessToken['tenant_access_token']=tat
    json_util.json_to_file(feiShuAccessToken,rf"D:\proj\private-conf\feiShuAccessToken.json")

print('tat')
print(tat)
# print(tat)
"""
resp_json
{'code': 99991672, 'msg': 'No permission', 
'error': {
    'message': 'Refer to the documentation to fix the error: https://open.feishu.cn/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-fix-the-99991672-error', 
'log_id': '20230321124302FF1094ABA822623682A1'}}
"""
# 获取通讯录自定义字段id
header = {"content-type":"application/json",
          "Authorization":"Bearer " + str(tat)}
url = "https://open.feishu.cn/open-apis/contact/v1/tenant/custom_attr/get"
r = requests.get(url, headers = header)
resp_json=r.json()
print("resp_json")
print(resp_json)

qq_id = list(resp_json["data"]["custom_attrs"].keys())[0]
sn_id = list(resp_json["data"]["custom_attrs"].keys())[1]
print("r.json()" )
print(r.json() )
print("sn_id")
print(sn_id)
print("qq_id")
print(qq_id)

# 获取部门id
department = {}
sex = {"男":"1", "女":"2"}
url = "https://open.feishu.cn/open-apis/contact/v1/scope/get"
r = requests.get(url, headers = header)
ls = r.json()["data"]["authed_departments"]
for i in range(len(ls)):
    url = "https://open.feishu.cn/open-apis/contact/v1/department/info/get?department_id=" + str(ls[i])
    r = requests.get(url, headers = header)
    name = r.json()["data"]["department_info"]["name"]
    department[name] = ls[i]

print("department")
print(department)

# 批量导入联系人信息
# url = "https://open.feishu.cn/open-apis/contact/v1/user/add"
# data = pd.read_excel('class_data.xlsx')
# data = data.iloc[2:, :]
# data = data.to_numpy()
# for i in range(len(data)):
#     user_data = {
#             "name":data[i][0],
#             "department_ids":[department[data[i][4][:7]]],
# #             "email":"zhangsan@gmail.com",
#             "mobile":"+86"+str(data[i][5]),
#             "mobile_visible":"true",
#             "city":data[i][7],
#             "country": "CN",
#             "gender":sex[data[i][1]],
#             "employee_type":1,
#             "employee_id":"id_" + str(data[i][3]),
#             "employee_no":str(data[i][3]),
#             "need_send_notification":"true",
#             "custom_attrs":{
#                 qq_id: {
#                     "value": str(data[i][6])
#                 },
#                 sn_id: {
#                     "value": str(data[i][3])
#                 }
#             }
#         }
#     data_to_send = json.dumps(user_data).encode("utf-8")
#     r = requests.post(url, data = data_to_send, headers = header)
#     print(r.json())