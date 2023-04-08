argsWenHao="""
table_schema= ? and table_name = ?"""

# argsList=[]

argsWenHao=argsWenHao.strip()

argsWenHaoList=argsWenHao.split("and")

def keyValShow(keyVal):
    keyValSps=keyVal.split("=")
    key=keyValSps[0].strip()
    val=keyValSps[1].strip()
    return key,val


for i in argsWenHaoList:
    # print(i)
    key,val=keyValShow(i)
    # print(key,val)
    Param=f'@Param("{key}") String  {key} ,'
    print(Param)

# @Param("table_schema") String  table_schema ,
# @Param("table_name") String  table_name ,