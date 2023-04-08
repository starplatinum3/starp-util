

#  file = open(path, encoding='gb18030'）
# 
    # try:
    #     with open(filepath, "r",encoding="utf-8") as fp:
    #         # string=fp.read()


import codecs
import sys
import time


def read_file(filepath,encoding="utf-8"):
    try:
        with open(filepath, "r",encoding=encoding) as fp:
            string=fp.read()
            return string
    except Exception as e:
        print(e)
        print("filepath")
        print(filepath)
        return None


"""
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的”ctime”。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
————————————————
版权声明：本文为CSDN博主「月尽天明_」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/huiyanshizhu/article/details/81277555
"""
def show_time(time_int):
    # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(test_stat.st_mtime))
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_int))
#     python 查看、修改文件属性_月尽天明_的博客-CSDN博客_python查看文件属性
# https://blog.csdn.net/huiyanshizhu/article/details/81277555

import os
def show_stat_of_path(path):
    stat=os.stat(path)
    last_modify_time=show_time(stat.st_mtime)
    # last_modify_time=show_time(stat.st_uid)
    # s=show_time(stat.st_size)
    print("last_modify_time",last_modify_time)
    # st_ctime
    create_time=show_time(stat.st_ctime)
    print("create_time",create_time)
    size=stat.st_size
    # print(size,"",size/1000,"M",size/1000/1000,"G")
    print(size,"B",size/1000,"K",size/1000/1000,"M",size/1000/1000/1000,"G")

def help_output(help_element,filename = 'help.txt'):
    # filename = 'help.txt'

    stdout = sys.stdout
    out_file = open(filename, 'w+',encoding='utf-8')
    sys.stdout = out_file

    help(help_element)
    out_file.flush()

    out_file.close()
    sys.stdout = stdout
# srcfile 需要复制、移动的文件   
# dstpath 目的地址


import csv

import pandas as pd


def getAllFilesOfWalk(dir):
    """使用listdir循环遍历"""
    if not os.path.isdir(dir):
        print (dir)
        return
    dirlist = os.walk(dir)
    # print("dirlist")
    # print(dirlist)
    abs_path_list=[]
    for root, dirs, files in dirlist:
        for file in files:
            # if file == className+'.java':
            if "考试" in file:

                abs_path=os.path.join(root,file)
                # print(abs_path)
                # os.system('idea64 '+abs_path)
                abs_path_list.append(abs_path)

                # file_path_lst.append(abs_path)
    return abs_path_list


# def dd(records):
#     df=pd.DataFrame.from_records(records)
#  数据列名
def to_csv(datas,file_name,encoding='utf-8-sig',mode='w'):
    # header = ['name', 'age'],
    # # header = ['name', 'age'] #数据列名
    # datas = [{'name': 'Tony', 'age': 17},
    #         {'name': '李华', 'age': 21}] # 字典数据
    # python 写出 csv 某几列 
    # dict 的列表转化为 dateframe
    header=datas[0].keys()
    # pd.DataFrame.from_records(data)
# 
    # test.csv表示如果在当前目录下没有此文件的话，则创建一个csv文件
    # a表示以“追加”的形式写入，如果是“w”的话，表示在写入之前会清空原文件中的数据
    # newline是数据之间不加空行
    # encoding='utf-8'表示编码格式为utf-8，如果不希望在excel中打开csv文件出现中文乱码的话，将其去掉不写也行。
    with open(file_name,mode= mode, newline='',encoding=encoding) as f: 
        # f.write(codecs.BOM_UTF8)
        writer = csv.DictWriter(f,fieldnames=header) # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        # writer.write(codecs.BOM_UTF8)
        writer.writeheader()  # 写入列名
        
        writer.writerows(datas) # 写入数据


import os
import shutil
# from glob import glob

# "D:\好活.txt"
 
def move_file(srcfile,dstpath):                       # 移动函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        abs_dst_path=os.path.join(dstpath,fname)
        # shutil.move(srcfile, dstpath + fname)          # 移动文件
        shutil.move(srcfile,abs_dst_path)  
        # print ("move %s -> %s"%(srcfile, dstpath + fname))
        print ("move %s -> %s"%(srcfile, abs_dst_path))

 
def move_file_no_add_dir(srcfile,dstpath):                       # 移动函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        abs_dst_path=os.path.join(dstpath,fname)
        # shutil.move(srcfile, dstpath + fname)          # 移动文件
        shutil.move(srcfile,abs_dst_path)  
        # print ("move %s -> %s"%(srcfile, dstpath + fname))
        print ("move %s -> %s"%(srcfile, abs_dst_path))
 
# src_dir = './'
# dst_dir = './move/'                                    # 目的路径记得加斜杠
# src_file_list = glob(src_dir + '*')                    # glob获得路径下所有文件，可根据需要修改
# for srcfile in src_file_list:
#     mymovefile(srcfile, dst_dir)                       # 移动文件

def show_stat(stat):
    last_modify_time=show_time(stat.st_mtime)
    # last_modify_time=show_time(stat.st_uid)
    # s=show_time(stat.st_size)
    print("last_modify_time",last_modify_time)
    size=stat.st_size
    # print(size,"",size/1000,"M",size/1000/1000,"G")
    print(size,"B",size/1000,"K",size/1000/1000,"M",size/1000/1000/1000,"G")
    # st_size=250167437



encoding_list=['utf-8','gbk','gb18030',]


def read_file_try(filepath):
    for encoding in encoding_list:
        string=read_file(filepath,encoding=encoding)
        if string:
            return string

def taoBao_json_move():
    dir_name=rf"D:\download"
    to_dir_name=rf"D:\taoBao"
    for i in os.listdir(dir_name):
        # "D:\taoBao\taobao_ 杏仁_2023_2_6_8_43_5.json"
        if i.startswith("taobao") and i.endswith(".json"):
            abs_from_file=os.path.join(dir_name,i)
            abs_to_file=os.path.join(to_dir_name,i)
            shutil.move(abs_from_file,abs_to_file)  
# mai 

def remove_tao_bao_dirs():
    taoBao_dir_name=rf"D:\taoBao"
    # for i in os.listdir(dir_name):
    #     # "D:\taoBao\taobao_ 杏仁_2023_2_6_8_43_5.json"
    #     if i.startswith("taobao") and i.endswith(".json"):
    #         abs_from_file=os.path.join(dir_name,i)
    #         abs_to_file=os.path.join(to_dir_name,i)
    #         shutil.move(abs_from_file,abs_to_file)  
    #         # move_file(abs_from_dir,abs_to_dir)
    #         # D:\taoBao

    # D:\taoBaoOut
    taoBaoOut_dir_name=rf"D:\taoBaoOut"
    # 'D:\\taoBao\\taobao_ 杏仁_2023_3_18_8_47_21.json'
    # res=os.removedirs('D:\\taoBao\\taobao_ 杏仁_2023_3_18_8_47_21.json')
    # print("res",res)
    for i in os.listdir(taoBao_dir_name):
        # if 
        # print(i)
        abs_json_dir_path_from=os.path.join(taoBao_dir_name,i)
        
        if os.path.isdir(abs_json_dir_path_from):
            abs_json_path=os.path.join(taoBao_dir_name,i,i)
            abs_json_path_to=os.path.join(taoBaoOut_dir_name,i)
            # shutil.move(abs_json_path,abs_json_path_to)  
            # print("abs_json_path",)
            # print(abs_json_path,abs_json_path_to)
            # os.remove(abs_json_dir_path_from)
            # os.remove(abs_json_dir_path_from)
            os.removedirs(abs_json_dir_path_from)
            print(abs_json_dir_path_from)

            
if __name__ == "__main__":
    # "D:\好活.txt"
    # move_file("D:\好活.txt",rf"D:\file")
    # file 
    # data=read_file("D:\好活.txt")
    # print(data)
    # abs_path_list=getAllFilesOfWalk(rf"D:\毕设")
    # for i in abs_path_list:
    #     print(i)
    # dir_name=rf"D:\download"
    # to_dir_name=rf"D:\taoBao"
    taoBao_dir_name=rf"D:\taoBao"
    # for i in os.listdir(dir_name):
    #     # "D:\taoBao\taobao_ 杏仁_2023_2_6_8_43_5.json"
    #     if i.startswith("taobao") and i.endswith(".json"):
    #         abs_from_file=os.path.join(dir_name,i)
    #         abs_to_file=os.path.join(to_dir_name,i)
    #         shutil.move(abs_from_file,abs_to_file)  
    #         # move_file(abs_from_dir,abs_to_dir)
    #         # D:\taoBao

    # D:\taoBaoOut
    taoBaoOut_dir_name=rf"D:\taoBaoOut"
    # 'D:\\taoBao\\taobao_ 杏仁_2023_3_18_8_47_21.json'
    # res=os.removedirs('D:\\taoBao\\taobao_ 杏仁_2023_3_18_8_47_21.json')
    # print("res",res)
    for i in os.listdir(taoBao_dir_name):
        # if 
        # print(i)
        abs_json_dir_path_from=os.path.join(taoBao_dir_name,i)
        
        if os.path.isdir(abs_json_dir_path_from):
            abs_json_path=os.path.join(taoBao_dir_name,i,i)
            abs_json_path_to=os.path.join(taoBaoOut_dir_name,i)
            # shutil.move(abs_json_path,abs_json_path_to)  
            # print("abs_json_path",)
            # print(abs_json_path,abs_json_path_to)
            # os.remove(abs_json_dir_path_from)
            # os.remove(abs_json_dir_path_from)
            os.removedirs(abs_json_dir_path_from)
            print(abs_json_dir_path_from)