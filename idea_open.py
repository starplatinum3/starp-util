

className='RestAuthenticationSuccessHandler'

import os 
# dir =r'D:\proj\springBoot\exam-sys-db2'

dir =r'D:\proj\springBoot\exam-sys-db2\src\main\java\com\starp\exam'
# for i in os.listdir(dir):
#     abs_path=os.path.join(dir,i)


def getallfilesofwalk(dir):
    """使用listdir循环遍历"""
    if not os.path.isdir(dir):
        print (dir)
        return
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            if file == className+'.java':

                abs_path=os.path.join(root,file)
                print(abs_path)
                os.system('idea64 '+abs_path)

getallfilesofwalk(dir)