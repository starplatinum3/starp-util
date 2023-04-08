

# 工科

# d 
majors=['工科','商学院','工商','旅游','资评','金融学','全院','国际贸易','金融学（中新合作办学）'
        '金融专业','资产评估专业','CFA', '金融学（CFA方向）','CMA实验班','经管'
        'CMA','国际经济与贸易','国际商务','Finance','UW','UW联合学院','中新合作办学','CFA','实验班'
        ,'Finance in NZUWI']
# {'商学院所有专业', '工商、旅游、资评等专业', '金融学（CFA方向）', '全院工科各专业', '金融学（中新合作办学）', 
# '金融专业
# 、资产评估专业', '国际贸易', 'CMA实验班', 'CMA', '国际经济与贸易、国际商务等经管专业',
#  'UW联合学院金融专业', '国际贸易、国际商务等专业', 'Finance in NZUWI', '国际经济与贸易',
#  '国际贸易、国际商务等', 'Finance'}
# main_applicable_majors

# D:\brain\2023_03_22_16_25_59\01 教学大纲- 大学物理(I)_2023_03_22_16_26_05.json

json_dir="D:\\brain\\2023_03_22_16_25_59\\"

import os
# for 
main_applicable_majors_list=[]
main_applicable_majors_set=set()

# main_applicable_majors_list[0]={}

# obj=main_applicable_majors_list[1]
# obj=None
# obj[i][j] =0
# # id 

# obj[i]=0
# obj.name=1


import json_util
for i in os.listdir(json_dir):
    abs_path=os.path.join(json_dir,i)
    data=json_util.file_path_to_dict(abs_path)
    # main_applicable_majors=data['main_applicable_majors']
    main_applicable_majors=data.get('main_applicable_majors',None)
    if main_applicable_majors is  None:
        continue
    if '工科' in main_applicable_majors:
        # print(data)
        basic_requirements=data.get('basic_requirements')
        print(basic_requirements)
        # 'basic_requirements'
    # if main_applicable_majors is not None:
    #     # print(main_applicable_majors)
    #     main_applicable_majors_set.add(main_applicable_majors)
    main_applicable_majors_set.add(main_applicable_majors)
print(main_applicable_majors_set)

