# doThing="select_information_schema_columns"
# doThing="select_limit_10"
# doThing="select_by_content_like"
# doThing="autoPaper"
# doThing="saveNew"

# doThing="saveQuestionDraw"

doThing="findAllEsQuestion"
# doThing="selectBySql"

from time_util import get_now_time_str

this_list=doThing.replace("select_","")
# print(f'    <el-button type="" @click="{doThing}_do">{doThing}_do</el-button>')

with open(r"codeGen\template\vueDoMethod.vue","r",encoding='utf-8') as f:
    template=f.read()
    code=template.replace("#doThing#",doThing)
    code=code.replace("#this_list#",this_list)

print("\n\n")
print(code)

# codePostDo=f"""
# {doThing}: (data) => post('/api/all/{doThing}',data), """
# print("\n\n")

# time_util 
# print(codePostDo)

codeGenDir=r"D:\codeGenVuePost"
# wi 

import os 

time_dir=get_now_time_str()

abs_dir=os.path.join(codeGenDir,time_dir)
os.makedirs(abs_dir)
abs_path=os.path.join(codeGenDir,time_dir,"vueDoMethod.vue")

with open(abs_path,"w+",encoding="utf-8") as f:
    f.write(code)

print("abs_path",abs_path)

# item_name=this_list.replace("select_","")
# vue_list_show_code=f"""

# {this_list}
#    <div @click="changeTableName(item)"
#      :key="item" v-for="item in {this_list}">
#       {{item}}
#     </div>"""

# print("\n\n")

# print(vue_list_show_code)

# vscode 代码提示 插件