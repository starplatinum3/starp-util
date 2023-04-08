
import json


def json_obj_to_str(json_obj):
    json_str=json.dumps(json_obj)
    return json_str


def str_to_json_obj(json_str):
    return json.loads(json_str)
   
def json_to_file(json_obj,filename):
    with open(filename, "w",encoding='utf-8') as fp:
        json.dump(json_obj, fp,ensure_ascii=False)
        # str to json python
        # json.dump 全是 u 

# file_util.read_file_try(dir_name)
import file_util
def file_path_to_dict(filepath):
    #  file = open(path, encoding='gb18030'）
#   
    string=file_util.read_file_try(filepath)
    # try:
    #     with open(filepath, "r",encoding="utf-8") as fp:
    #         string=fp.read()
    # except Exception as e:
    #     print(e)
    #     print("filepath")
    #     print(filepath)
    #     with open(filepath, "r",encoding="gbk") as fp:
    #         string=fp.read()
    dict_data = json.loads(string)
    return dict_data
    #     json.dump(json_obj, fp)
    # country = '{"name": "United States", "population": 331002651}'
    # country_dict = json.loads(country)