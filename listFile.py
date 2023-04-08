
import os
import time 

# dir_name=r'E:\phoneFIle'
# dir_name=r'E:\download'
# dir_name=r'E:\phone2'
# E:\pic
# dir_name=r'E:\pic'

# dir_name=r'E:\\'
# E:\edgeDownload
# dir_name=r'E:\edgeDownload'
# dir_name_one='edgeDownload'

# dir_name_one='phoneFIle'
dir_name_one='多的'
like_str="绩点"

# E:\多的
dir_name=rf'E:\{dir_name_one}'

# E:\phone2
# out_file_name=r"D:\phoneFIle.txt"
# out_file_name=r"D:\download_e.txt"
# out_file_name=r"D:\phone2_e.txt"
# out_file_name=r"D:\pic_e.txt"
# out_file_name=r"D:\disk_e.txt"
out_file_name=rf"D:\{dir_name_one}_e.txt"



# phoneFIleDir=os.listdir(dir_name)
# 22 26

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

def show_stat(stat):
    last_modify_time=show_time(stat.st_mtime)
    # last_modify_time=show_time(stat.st_uid)
    # s=show_time(stat.st_size)
    print("last_modify_time",last_modify_time)
    size=stat.st_size
    # print(size,"",size/1000,"M",size/1000/1000,"G")
    print(size,"B",size/1000,"K",size/1000/1000,"M",size/1000/1000/1000,"G")
    # st_size=250167437

def show_dir(abs_dir,dir_name_this):
    file_names=[]
    listDir=os.listdir(abs_dir)
    # E:\phoneFIle
    for fileName in listDir:
        # file_names. 
        # abs_file_path=os.path.join(dir_name,fileName)
        abs_file_path=os.path.join(abs_dir,fileName)
        # abs_file_path=os.path.join(dir_name_this,fileName)
        file_names.append(abs_file_path)
        # if fileName.startswith("cn"):
        #     print("cn ")
        #     print(fileName)
        # if "奖学金" in fileName:
        #     print(abs_file_path)
        # if "头像" in fileName:
        #     print(abs_file_path)
        if like_str in fileName:
            print(abs_file_path)
        # if ".jpg" in fileName:
        #     print(abs_file_path)
        # if fileName.endswith(".iso"):
        #     # print("iso ")
        #     print(fileName)
        # if fileName.endswith(".iso"):
        #     print("iso ")
        #     print(fileName)

    # if fileName.endswith(".mp4"):
    #     print(fileName)
        
    #     # abs_dir=os.path.join(phoneFIleDir,fileName)
    #     stat=os.stat(abs_file_path)
    #     print(stat)
    #     # last_modify_time=show_time(stat.st_mtime)
    #     # print("last_modify_time",last_modify_time)
    #     show_stat(stat)


        # os.stat(fileName)
    # if "bandi" in fileName:
    #     print(fileName)
    # os.stat('package-lock.json')
    # os.stat(fileName)

# os.stat_result(st_mode=33206, st_ino=844424933349774, st_dev=3425131161, st_nlink=1, st_uid=0, st_gid=0, st_size=250167437, st_
# atime=1675585066, st_mtime=1672891987, st_ctime=1672888835)

# time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(test_stat.st_mtime))

    file_names_article="\n".join(file_names)
    # print(file_names_article)
    # download
    # out_file_name
    # "phoneFIle.txt"
    # dir_name_this
    out_file_name=f"D:/{dir_name_this}_e.txt"
    # print("out_file_name",out_file_name)
    # print("file_names_article",file_names_article)
    # with open(out_file_name,"w",encoding="utf-8") as f:
    #     f.write(file_names_article)
    # to_file
# iso
# macOS Catalina 10.15.5 (19F101).iso
# iso
# macOS Catalina 10.15.5 (19F101).iso
#  os.listdir 判断 是dir 
# disk_name=r"E:\\"
# disk_name="E:\\"
# D:\
# D:\D:\
# disk_name="D:\\"
# disk_name=rf"D:\download"

# disk_name=rf"G:\addd"
# G:\
# abs_path G:\\视力
# 两个 apk 
disk_name=rf"G:\\"

# abs_path G:\addd\浙大城市学院大学生创新训练管理系统 视力.mhtml
# D:\download
# disk_name="D:\\download"
# D:\
error_file_list=[]
keyword="视力"
# "教学大纲"
# abs_path D:\视力
for file_name in os.listdir(disk_name):
    # file_name.
    abs_path=os.path.join(disk_name,file_name)
    if keyword in file_name:
        # print("file_name",file_name)
        print("abs_path",abs_path)
    # abs_path=os.path.join(disk_name,file_name)
    if os.path.isdir(abs_path):
        # print("abs_path",abs_path)
        try:
            show_dir(abs_path,file_name)
        except Exception as e:
            print(e)
            # print("file_name")
            # print(file_name)
            error_file_list.append(file_name)

print("error_file_list",error_file_list)
# show_dir(phoneFIleDir)

# for root, dirs, files in os.walk(disk_name):  
#     print(root) #当前目录路径  
#     print(dirs) #当前路径下所有子目录  
#     print(files) #当前路径下所有非目录子文件
#     for dir_name in dirs:
#         print("dir_name",dir_name)
#         # show_dir()

import string_util

# string_util.chinese_word

import strUtil
# strUtil.strUtil.show_str("中文")