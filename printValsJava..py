str="""
singleArray.length  qustionNum"""

str=str.strip()
import  listUtil
sps=str.split(" ")
sps=listUtil.remove_none(sps)
# listUtil.printList(sps)
for i in sps:
    print(f'System.out.println("{i}");')
    print(f'System.out.println({i});')
# print(sps)