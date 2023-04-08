

# D:\weixinData\WeChat Files\wxid_6u05k4dt9r8e22\FileStorage\File

file_dir=rf'D:\weixinData\WeChat Files\wxid_6u05k4dt9r8e22\FileStorage\File'

import os

# D:\毕设
file_path_lst=[]

def getAllFilesOfWalk(dir):
    """使用listdir循环遍历"""
    if not os.path.isdir(dir):
        print (dir)
        return
    dirlist = os.walk(dir)
    # print("dirlist")
    # print(dirlist)
    for root, dirs, files in dirlist:
        for file in files:
            # if file == className+'.java':
            if "开题" in file:

                abs_path=os.path.join(root,file)
                print(abs_path)
                # os.system('idea64 '+abs_path)

                # file_path_lst.append(abs_path)

import  json_util

# json_util.json_to_file(file_path_lst,rf'D:\file_path_lst_wechat.json')
# i 

getAllFilesOfWalk(file_dir)
# json_util.json_to_file(file_path_lst,rf'D:\file_path_lst_wechat.json')
# 