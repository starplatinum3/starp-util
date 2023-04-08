# Python3 将GBK转换成utf-8编码，明天继续实现，把*.java文件 *.porperties文件都转成utf-8
import codecs
from logging.handlers import RotatingFileHandler


def ReadFile(filePath, encoding="gbk"):
    try:
        with codecs.open(filePath, "r", encoding) as f:
            return f.read()
    except Exception as e:
        print(filePath,"不是",encoding)
        return None



def WriteFile(filePath, data, encoding="utf-8"):
    with codecs.open(filePath, "w+", encoding) as f:
        f.write(data)


def UTF8_2_GBK(src, dst):
    content = ReadFile(src, encoding="gbk")
    WriteFile(dst, content, encoding="utf-8")

def gbk_to_utf8(src, dst):
    content = ReadFile(src, encoding="gbk")
    if None==content:
        return
    WriteFile(dst, content, encoding="utf-8")



import os
import os.path

def str_end_with_in_list(string:str,end_with_list):
    for i in end_with_list:
        if(string.endswith(i)):
            return True
    return False

# 递归遍历rootdir目录，把目录中的*.java编码由gbk转换为utf-8
def ReadDirectoryFile(rootdir,end_with_list,out_root):
    fail_lst=[]
    from_path_lst=[]
    to_abs_lst=[]
    for parent, dirnames, filenames in os.walk(rootdir):
        # case 1:
        for dirname in dirnames:
            pass
            # print("parent folder is:" + parent)
            # print("dirname is:" + dirname)
        # case 2
        for filename in filenames:
            # print("parent folder is:" + parent)
            # print("filename with full path:" + os.path.join(parent, filename))
            # if filename.endswith(".cpp"):
            if(str_end_with_in_list(filename,end_with_list)):
        
            # if filename.endswith(".java"):
                
                from_abs=os.path.join(parent, filename)
                to_abs=os.path.join(out_root,parent, filename)
                # ReadFile(from_abs,"utf-8")
                from_path_lst.append(from_abs)
                to_abs_lst.append(to_abs)
                try:
                    # UTF8_2_GBK(os.path.join(parent, filename), os.path.join(parent, filename))
                    # UTF8_2_GBK(from_abs, to_abs)
                    # gbk_to_utf8(from_abs, to_abs)
                    pass
                # print("Java文件")
                except:
                    fail_lst.append(from_abs)
    print("from_path_lst",from_path_lst)
    print("to_abs_lst",to_abs_lst)
    print("fail_lst",fail_lst)


end_with_list=[".cpp",".java"]

# import myfile
from myfile import backup_proj_src, copyfile_lst,get_src_dst_list_re

# from pathlib import Path

# path1 = Path(r"C:\folder\subfolder\myfile.txt")
# path2 = Path(r"C:\Myfile.txt")
# print(path1.parent)
# print(path2.parent)

if __name__ == "__main__":
    # ReadDirectoryFile(".")
    
    # root_dir=r"G:\project\javaProj\eclipse_20_08\ccrental\src\cn\edu\zucc\personplan"
    # root_dir=r"D:\proj\cpp\data-struct-code-cpp"
    # G:\project\Android\GameHall_Android2
    # root_dir=r"D:\proj\Android\安卓物理小球滚动游戏源码_爱给网_aigei_com\安卓物理小球滚动游戏源码"
    # dst_path=r"D:\proj\Android\安卓物理小球滚动游戏源码_爱给网_aigei_com\安卓物理小球滚动游戏源码"

    # root_dir=r"G:\project\Android\GameHall_Android2"
    # dst_path=r"G:\project\Android\GameHall_Android2_bak"

    # root_dir=r"G:\project\Android\GameHall_Android2_bak"
    # dst_path=r"G:\project\Android\GameHall_Android2_bak2"

    # root_dir=r"G:\project\Android\GameHall_Android2_bak2"
    # # dst_path=r"G:\project\Android\GameHall_Android2_bak3"
    # back_dir=r"G:\project\Android\GameHall_Android2_bak3"

    # root_dir=r"D:\project\waibao\what-rubbish-final\app\src\main\java\com\bn\tl\anzhi"
    # back_dir=r"D:\project\waibao\what-rubbish-final-bak\utf-8-2\app\src\main\java\com\bn\tl\anzhi"

    # root_dir=r"G:\project\javaProj\lanqiao\src\lanqiao"
    # back_dir=r"D:\lanqiaoCode"
    # root_dir=r"D:\proj\cpp\cs-system-principle"
    # back_dir=r"D:\proj\cpp\cs-system-principle-utf-8"
    # 会写道 utf -8 的目录 是新的 不会覆盖之前的项目吧 

    # root_dir=r"D:\proj\compile\SchoolCode"
    # back_dir=r"D:\proj\compile\SchoolCode-utf8"

    root_dir=r"D:\proj\bishe\genetic_algorithm_generating_system"
    back_dir=r"D:\proj\bishe\genetic_algorithm_generating_system-utf8"

    
    # python 判断path 在不在
        # import os.path
        
    if not os.path.exists(back_dir):
        print("没有备份目录，创建目录",back_dir)
        # os.mkdirs(back_dir)
        os.makedirs(back_dir)
        # makedirs

    # os.path.ispa
    # os.mkdirs(back_dir)
    from_lst=[]
    to_lst=[]
    ignore_dir_lst=[".git"]
    re_lst=None
    # 全部都要
    get_src_dst_list_re(root_dir, back_dir, from_lst, to_lst,
                        ignore_dir_lst, re_lst)
    # backup_proj_src(root_dir,back_dir)
    # 先备份 有了文件
    print("root_dir",root_dir)
    print("back_dir",back_dir)
    copyfile_lst(from_lst,to_lst)

    print("from_lst",from_lst)
    print("to_lst",to_lst)

    # i=0
    # for f in from_lst:
    #     data=ReadFile(f)
    #     if data==None:
    #         continue
    #         i+=1
    #     WriteFile(to_lst[i], data)
    #     i+=1
    # 会写道 utf -8 的目录 是新的 不会覆盖之前的项目吧 
#     D:\proj\bishe\genetic_algorithm_generating_system\WebContent\file\系统说明.docx 不是 gbk
# Traceback (most recent call last):
#   File "d:\proj\python\my_util_py_pub\utf8.py", line 170, in <module>
#     data=f.read()
#   File "D:\software\anaconda\envs\py374\lib\codecs.py", line 322, in decode
#     (result, consumed) = self._buffer_decode(data, self.errors, final)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 14: invalid start byte

    for i in range(len(from_lst)):
        from_file=from_lst[i]
        to_file=to_lst[i]
        data=ReadFile(from_file)
        if data==None:
            with open(from_file,"r",encoding="utf-8") as f:
                data=f.read()
            # continue
        if data==None:
            continue
        # path1 = Path(to_file)
        # to_file.
        # dir=to_file.split("\\")[0:-1].join("\\")
        # print("dir",dir)
        # python 文件的父目录 路径
        # if not os.path.exists(to_file):
        #     print("没有目录，创建目录",to_file)
 
        #     os.makedirs(to_file)
        WriteFile(to_file, data)
    
    # print("备份在",back_dir)
    # ReadDirectoryFile(root_dir,end_with_list,back_dir)
    
    print("end")
    # print("备份在",back_dir)
    print("输出utf-8",back_dir)
    # print("out here ",root_dir)