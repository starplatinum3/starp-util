

out_file=rf"D:\proj\job\error_file_list_companyNature_error.json"

import json_util

data=json_util.file_path_to_dict(out_file)

error_file_dir=rf'D:\proj\job\24365_School_error_file_list_companyNature'
import file_util

for file_path in data:
    # file_name=file_path.split('\\')[-1]
    file_util.move_file(file_path,error_file_dir)

# file_util.move_file(out_file,rf"D:\proj\job\error_file_list_companyNature_error\error_file_list_companyNature_error.json")

# D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\error_file_list_companyNature_error_check.py"
# D:\proj\job\24365Scholl\24265_school_page_1000 (2).json
print(data[0])
# D:\proj\job\24365_School_error_file_list_companyNature
# 24365Scholl 
# md 24365_School_error_file_list_companyNature
print(len(data))
# 4299

# python 文件移动 到文件夹