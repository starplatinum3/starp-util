

# D:\proj\job\24365Scholl

file_dir=r'D:\proj\job\24365Scholl'

import os 

import json_util

def list_parse(lst):
    for obj in lst:
        # obj
        obj['jobLink']
        pass


for file_name in os.listdir(file_dir):
    # print(file_name)
    abs_path=os.path.join(file_dir,file_name)
    data=json_util.file_path_to_dict(abs_path)
