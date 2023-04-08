# D:\download\牛客网 - 找工作神器_笔试题库_面试经验_实习招聘内推，求职就业一站解决_牛客网_files

import os 
from shutil import copyfile

# dir_name=r"D:\download\牛客网 - 找工作神器_笔试题库_面试经验_实习招聘内推，求职就业一站解决_牛客网_files"
# dir_name=r"D:\download\2021小米集团校招笔试真题_测试开发工程师_牛客网_files"
dir_name=r"D:\download\对n个互不相同的符号进行哈夫曼编码。若生成的哈夫曼树共有35个结点，则n的值是：_中兴软件类笔试试卷A_牛客网_files"
list_dir=os.listdir(dir_name)

no_sufix_pic_list=[]
# copyfile(source, target)
def parse_no_sufix_pic(pic_name:str):
    if "." not in pic_name:
        # return pic_name
        print("not sufix pic",pic_name)
        # pic_name=pic_name+".png"
        no_sufix_pic_list.append(pic_name)
        return ""
    idx=pic_name.index(".")
    print(idx)

# 文件copy python

do_copy=False
for i in list_dir:
    # print(i)
    pic_name=i
    if "." not in pic_name:
        print("not sufix pic",pic_name)
        abs_src_path=os.path.join(dir_name,i)
        abs_target_path=os.path.join(dir_name,i+".png")
        if do_copy:
            copyfile(abs_src_path, abs_target_path)
        no_sufix_pic_list.append(pic_name)
    # parse_no_sufix_pic(i)

print(no_sufix_pic_list)

# not sufix pic 33ED1936567FB5A523ED63D6C451B84B
# not sufix pic 504104551_1598686287835_605475850F555A9A1D76953CFB3E39A6
# not sufix pic 59_1534321710941_41A541F87AE349E1D829B1B0B95C955D
# not sufix pic 605475850F555A9A1D76953CFB3E39A6
# not sufix pic 7402D8581CBE60E6F7092E8BE138892C
# not sufix pic 7402D8581CBE60E6F7092E8BE138892C(1)
# not sufix pic 889007829_1569925458763_025D697BCBE26745C4064EE75FB3AA64
# not sufix pic 988853361_1587444012178_F8F0018520378C61FF00245490884E5E
# not sufix pic FECD76F09C4EFFA7102ECDBC1795FB3B
# []