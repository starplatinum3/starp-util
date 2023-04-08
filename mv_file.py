
import shutil



# origin_dir=rf'D:\proj\python\my_util_py_pub'
# /etc/maven/settings.xml
origin_dir=rf'/etc/maven'

new_file_dir=rf'/home/work/app/my_util_py_pub'

back_up_dir=rf'/home/work/backup'


# origin_dir=rf'D:\proj\python\my_util_py_pub'
# # file_name='gugu.txt'
# file_name='settings.xml'
# # D:\proj\python\my_util_py_pub\settings.xml
# # D:\proj\python\my_util_py_pub\gugu.txt
# # file_name='merge_sql.py'

# # new_file_dir=rf'D:\proj\python'
# new_file_dir=rf'D:\download'

# back_up_dir=rf'D:\\'

file_name='settings.xml'

import os 
import time_util

now_time_str=time_util.get_now_time_str()

back_up_file_abs=os.path.join(back_up_dir,f'{file_name}_{now_time_str}')

print("back_up_file_abs")
print(back_up_file_abs)

origin_file_abs=os.path.join(origin_dir,file_name)
print("origin_file_abs")
print(origin_file_abs)

# print("origin_file_abs")
# print(origin_file_abs)
abs_new_file=os.path.join(new_file_dir,file_name)
print("abs_new_file")
print(abs_new_file)

shutil.move(origin_file_abs,back_up_file_abs)  
shutil.move(abs_new_file,origin_file_abs)
