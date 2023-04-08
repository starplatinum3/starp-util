# from urllib import request
import requests
import pip
# print(pip.pep425tags.get_supported())

supported_version_list=[]
def supported_tuple_list_show(supported_tuple_list):
    for supported_tuple  in  supported_tuple_list:
    # for supported_tuple  in  pip.pep425tags.get_supported():
        supported_version="-".join(supported_tuple)
        print(supported_version)
        supported_version_list.append(supported_version)
# D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\plaform_show.py"
# Traceback (most recent call last):
#   File "d:\proj\python\my_util_py_pub\plaform_show.py", line 2, in <module>
#     print(pip.pep425tags.get_supported())
# AttributeError: module 'pip' has no attribute 'pep425tags'

supported_tuple_list=[('cp36', 'cp36m', 'manylinux1_x86_64'), ('cp36', 'cp36m', 'linux_x86_64'), ('cp36', 'abi3', 'manylinux1_x86_64'), ('cp36', 'abi3', 'linux_x86_64'), ('cp36', 'none', 'manylinux1_x86_64'), ('cp36', 'none', 'linux_x86_64'), ('cp35', 'abi3', 'manylinux1_x86_64'), ('cp35', 'abi3', 'linux_x86_64'), ('cp34', 'abi3', 'manylinux1_x86_64'), ('cp34', 'abi3', 'linux_x86_64'), ('cp33', 'abi3', 'manylinux1_x86_64'), ('cp33', 'abi3', 'linux_x86_64'), ('cp32', 'abi3', 'manylinux1_x86_64'), ('cp32', 'abi3', 'linux_x86_64'), ('py3', 'none', 'manylinux1_x86_64'), ('py3', 'none', 'linux_x86_64'), ('cp36', 'none', 'any'), ('cp3', 'none', 'any'), ('py36', 'none', 'any'), ('py3', 'none', 'any'), ('py35', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), ('py31', 'none', 'any'), ('py30', 'none', 'any')]

supported_tuple_list_show(supported_tuple_list)
# for supported_tuple  in  pip.pep425tags.get_supported():
#     supported_version="-".join(supported_tuple)
#     print(supported_version)

# https://pypi.tuna.tsinghua.edu.cn/simple/opencv-contrib-python/
opencv_contrib_python_url="https://pypi.tuna.tsinghua.edu.cn/simple/opencv-contrib-python/"
# response = requests.get(opencv_contrib_python_url)

# print(response)
# print(response.text)

print(supported_version_list)