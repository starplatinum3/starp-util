


# D:\kanZhun\KanZhunCompanyLink_log.json


file_path=rf"D:\kanZhun\KanZhunCompanyLink_log.json"

import json_util

data=json_util.file_path_to_dict(file_path)
href_list=data['href_list']

# idx=4
idx=40
href=href_list[idx]
# https://www.kanzhun.com/firm/info/1n170t65Eg~~.html?idx=40
print(f"{href}?idx={idx}")