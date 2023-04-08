

import os 

# os.path.join("a","b")

# import insertIntoMongodb
import csv 

import pymongo
from pymongo import MongoClient         #导入MongoDb第三方库
connect = MongoClient('localhost')      #连接本地MongoDB服务器/127.0.0.1
# db = connect.mongo_demo                 #连接（创建）mongo_demo数据库
# employees = db.employees                #连接（创建）employees数据集
# employees.remove(None)                  #先清空一下数据集
# connect["mongo_demo"]["employees"].
mongo_demo=connect["mongo_demo"]
# employees=mongo_demo["employees"]

def list_all(collection):
    collection_find=collection.find()
    collection_find=list(collection_find)
    # print("collection_find")
    # print(collection_find)
    return collection_find

table=mongo_demo["table"]
# table=connect["table"]
table_find=list(table.find())
print("table_find")
print(table_find)
# [{'_id': ObjectId('6376fa6c147d34ac81f5e472'), 'name': 'jonathon', 'sex': 'male'}, {'_id': ObjectId('6376fa9b433074e24d334e45'), 'name': 'jonathon', 'sex': 'male'}]
# employees=mongo_demo["employees"]
def insertIntoMongodb(csv_file,set1):
    with open(csv_file,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        csv_data=[]
        for row in reader:
            # print(row)
            csv_data.append(row)
            # set1.add(row[0])
        set1.insert_many(csv_data)


dir=r"D:\csvData"

# set1=employees


# for fileName in os.listdir(dir):
#     # fileName=fileName.replace("_2022-10-2","")
#     colName=fileName.replace("_2022-10-2.csv","")
#     print("colName")
#     print(colName)
#     abs_path=os.path.join(dir,fileName)
#     # abs_path
#     print("abs_path")
#     print(abs_path)
#     col=mongo_demo[colName]
    
#     insertIntoMongodb(abs_path,col)