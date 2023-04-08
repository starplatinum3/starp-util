
# D:\download

import os 


key_words_list=['java',]
upper_money=15000
# upper_money=10000
# upper_money=25000
# upper_money=20000
abs_file_path_set=set()
link_set=set()

def  kan_zhun_CompanyLink_move():
    download_dir=rf"D:\download"

    import json_util

    href_list=[]
    error_list=[]
    for file_name in os.listdir(download_dir):
        # "D:\download\KanZhunCompanyLink_杭州大和热磁电子有限公司.json"
        if file_name.startswith('KanZhunCompanyLink'):
            abs_file_path=os.path.join(download_dir,file_name)
            if  abs_file_path==rf'D:\download\KanZhunCompanyLink_华数传媒控股股份有限公司 (1).json':
                continue
            try:
                print(abs_file_path)
                data=json_util.file_path_to_dict(abs_file_path)
                # href=data['href']
                href=data.get('href')
                if  href is None:
                    continue
                href_list.append(href)
            except Exception as e:
                print(e)
                error_list.append(abs_file_path)

    print("href_list")
    print(href_list)
    print("error_list")
    print(error_list)

    log_data={
    "href_list":  href_list,
        "error_list": error_list
    }

    import time_util
    now_time_str=time_util.get_now_time_str()

    # D:\kanZhun\KanZhunCompanyLink_log.json


    # json_util.json_to_file(log_data,rf"D:\kanZhun\KanZhunCompanyLink_log_{now_time_str}.json")
import json_util

import shutil

# kanZhunSalary
def  kan_zhun_Salary_move():
    to_dir="D:\\kanZhunDocSalary"
    # kanZhunSalary_https___www.
    download_dir=rf"D:\download"

 
    href_list=[]
    error_list=[]
    for file_name in os.listdir(download_dir):
        # "D:\download\KanZhunCompanyLink_杭州大和热磁电子有限公司.json"
        if file_name.startswith('kanZhunSalary'):
            abs_file_path=os.path.join(download_dir,file_name)
            if  abs_file_path==rf'D:\download\KanZhunCompanyLink_华数传媒控股股份有限公司 (1).json':
                continue
            try:
                # print(abs_file_path)
                # to_dir
                abs_to_file_path=os.path.join(to_dir,file_name)
                # shutil.move(abs_file_path,abs_to_file_path)
                print(f"move {abs_file_path} to {abs_to_file_path}")
                # data=json_util.file_path_to_dict(abs_file_path)
                # href=data['href']
                # href=data.get('href')
                # if  href is None:
                #     continue
                # href_list.append(href)
            except Exception as e:
                print(e)
                error_list.append(abs_file_path)

    # print("href_list")
    # print(href_list)
    # print("error_list")
    # print(error_list)

    # log_data={
    # "href_list":  href_list,
    #     "error_list": error_list,
        
    #       "to_dir": to_dir,
    # }

    import time_util
    now_time_str=time_util.get_now_time_str()

    # D:\kanZhun\KanZhunCompanyLink_log.json


    # json_util.json_to_file(log_data,rf"D:\kanZhun\KanZhunSalary_log_{now_time_str}.json")

def change_money_num(avg_salary):
    return int(avg_salary.replace('¥','').replace(',',''))
# ¥8,680 转化为  数字 python代码

job_name_set=set()


def file_path_to_http(file_path_of_link):
    # file_path_of_link=file_path_of_link[0]
    print("file_path_of_link")
    print(file_path_of_link)
    # https___
    # file_path_of_link.split('https___')
    end=file_path_of_link.split('https___')[-1]
    # end.split('.html_idx=')[0]
    end:str
    end=end.replace('.html_idx=','.html?idx=')
    end=end.replace('.json','')
    end=end.replace('_firm','/firm')
    end=end.replace('_wage','/wage')
    return "https://"+end
    # _firm
    # file_path.split('https___www.kanzhun.com_firm_wage_')[1].split('.html_idx=')[0]


# key_words_list=['开发','java','python','前端','测试']


def match_words(job_name):
    # job_name.upper()
    for key_word in key_words_list:
        if key_word in job_name.lower():
            return True
    return False

res_list=[]
# salary_list,
# upper_money=10000


company_name_set=set()
high_money_list=[]
def look_salary_list(abs_file_path,file_name):
    data=json_util.file_path_to_dict(abs_file_path)
    salary_list=data.get('salary_list')
    # avg_salary
    job_name_set_high_salary=set()
    title=data.get('title')
    for item in salary_list:
        # job_name
        job_name=item.get('job_name')
        # title
        if job_name is None:
            continue
        job_name_set.add(job_name)
        match_words_yes=match_words(job_name)
        # if '开发' in job_name:
        if match_words_yes:
            # print()
            
            avg_salary=item.get('avg_salary')
            avg_salary_num=change_money_num(avg_salary)
            
            if avg_salary_num>upper_money:
                item.update({'abs_file_path':abs_file_path})
                item.update({'company_name':title})
                job_name_set_high_salary.add(job_name)
                # print(abs_file_path)
                # print(item)
                res_list.append(item)
                company_name_set.add(title)
                https=file_path_to_http(file_name)
                link_set.add(https)
                abs_file_path_set.add(abs_file_path)
                
                # high_money_list.append({
                #     'company_name':title,
                # })
                # print(data)
    

def  kan_zhun_Salary_read():
    to_dir="D:\\kanZhunDocSalary"
    # kanZhunSalary_https___www.
    download_dir=rf"D:\download"
    # "job_name"

 
    href_list=[]
    error_list=[]
    
    for file_name in os.listdir(download_dir):
        # "D:\download\KanZhunCompanyLink_杭州大和热磁电子有限公司.json"
        if file_name.startswith('kanZhunSalary'):
            abs_file_path=os.path.join(download_dir,file_name)
            if  abs_file_path==rf'D:\download\KanZhunCompanyLink_华数传媒控股股份有限公司 (1).json':
                continue
            try:
                # print(abs_file_path)
                # to_dir
                # abs_to_file_path=os.path.join(to_dir,file_name)
                # salary_list
                # data=json_util.file_path_to_dict(abs_file_path)
                # salary_list=data.get('salary_list')
                # look_salary_list(   salary_list,abs_file_path)
                look_salary_list(   abs_file_path,file_name)
                # shutil.move(abs_file_path,abs_to_file_path)
                # print(f"move {abs_file_path} to {abs_to_file_path}")
                # data=json_util.file_path_to_dict(abs_file_path)
                # href=data['href']
                # href=data.get('href')
                # if  href is None:
                #     continue
                # href_list.append(href)
            except Exception as e:
                print(e)
                error_list.append(abs_file_path)

# kan_zhun_Salary_move()

kan_zhun_Salary_read()
# job_name
# {'job_name': '新媒体运营', 'contribution_quantity': '数据来自5名用户贡献', 'avg_salary': '¥6,560', 'compare': '40%', 'tootip': '¥6560', 'lowest_salary': '¥3200', 'highest_salary': '¥7400'}


print("job_name_set")
print(job_name_set)

import time_util
now_time_str=time_util.get_now_time_str()
# out_file_path=rf"D:\kanZhun\KanZhunSalary_job_name_set_{now_time_str}.json"
# "D:\\download\\kanZhunSalary_https___www.kanzhun.com_firm_wage_0X193N24Fg~~.html_idx=15.json", 
out_file_path=rf"D:\kanZhun\KanZhunSalary_log_{now_time_str}.json"


print("out_file_path")
print(out_file_path)

log_data={
    'KanZhunSalary_list':res_list,
    'upper_money':upper_money,
    'company_name_set':list(company_name_set),
    'key_words_list':key_words_list,
    'abs_file_path_set':list(abs_file_path_set),
    'link_set':list(link_set),
}
# json_util.json_to_file(res_list,out_file_path)
json_util.json_to_file(log_data,out_file_path)
file_path_kanZhun="kanZhunSalary_https___www.kanzhun.com_firm_wage_0X193N24Fg~~.html_idx=15.json", 

# file_path_kanZhun="D:\\download\\kanZhunSalary_https___www.kanzhun.com_firm_wage_0X193N24Fg~~.html_idx=15.json", 
# out_file_path=rf"D:\kanZhun\KanZhunSalary_log_{now_time_str}.json"

# http_link=file_path_to_http(file_path_kanZhun)
# print(http_link)
