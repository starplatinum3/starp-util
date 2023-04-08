
dir=r'D:\proj\bishe\exam-sys-comunity\src\main\java\com\example\community'

import os
# domain
domain="domain"
entity="entity"

def get_filenames(dir_name):
    domain_path=os.path.join(dir,dir_name)
    domain_path_file_list=[]
    for domain_path_file in os.listdir(domain_path):
        # print(domain_path_file)
        domain_path_file_list.append(domain_path_file)
    return domain_path_file_list


# domain_path=os.path.join(dir,domain)

# for domain_path_file in domain_path:
#     print(domain_path_file)

domain_filenames=get_filenames(domain)

entity_filenames=get_filenames(entity)

# python 两个列表 相同的 
import listUtil

# listUtil.duplicate(domain_filenames,entity_filenames)
dup_in_two_list_entity=listUtil.dup_in_two_list(domain_filenames,entity_filenames)
# dup_in_two_list

print(dup_in_two_list_entity)

# {'Message.java', 'Tenant.java', 'Draw.java', 'Question.java', 'Component.java', 'User.java', 'TextContent.java'}