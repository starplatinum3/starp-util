
str="""
colName
admin
abs_pa
c:liad
colName
admin
abs_pa
c:liad
"""
str=str.strip()

lines=str.split("\n")

list=[]
idx=0
for line in lines:
    idx+=1
    if idx==2:
        list.append(line)
    if idx==4:
        idx=0

print(list)
