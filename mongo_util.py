

import json_util

def conf_path_to_mongodb_url(conf_path):
  mongodbJobDetail_conf=json_util.file_path_to_dict(conf_path)
  url=rf"mongodb://{mongodbJobDetail_conf['username']}:{mongodbJobDetail_conf['password']}@{mongodbJobDetail_conf['host']}:27017/{mongodbJobDetail_conf['db_name']}?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
  return url

def like(word='大纲'):
    doc_name_regex = f'.*{word}.*'
    return {'$regex': doc_name_regex}

"""
{
  "username": "root",
  "password": ".",
  "host":"10...",
  "db_name":""
}

"""
# mongodbJobDetail_conf['username']
# D:\home\app\private-conf\mongodbJobDetail.json