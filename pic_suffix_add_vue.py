

# D:\proj\springBoot\xzs-mysql\source\vue\xzs-student\src\views\exam\paper\do.vue

filepath=r"D:\proj\springBoot\xzs-mysql\source\vue\xzs-student\src\views\exam\paper\do.vue"
filenames=['59_1534321710941_41A541F87AE349E1D829B1B0B95C955D', '889007829_1569925458763_025D697BCBE26745C4064EE75FB3AA64']   
# filenames=['33ED1936567FB5A523ED63D6C451B84B', '504104551_1598686287835_605475850F555A9A1D76953CFB3E39A6', '59_1534321710941_41A541F87AE349E1D829B1B0B95C955D', '605475850F555A9A1D76953CFB3E39A6', '7402D8581CBE60E6F7092E8BE138892C', '7402D8581CBE60E6F7092E8BE138892C(1)', '889007829_1569925458763_025D697BCBE26745C4064EE75FB3AA64', '988853361_1587444012178_F8F0018520378C61FF00245490884E5E', 'FECD76F09C4EFFA7102ECDBC1795FB3B']
with open(filepath, "r", encoding="utf-8") as f:
    data=f.read()
    # lines=f.readlines()
    # for line in lines:
    #     if line.find("this.$emit")!=-1:
    #         print(line)

# replace 如果有后缀 就不 
for filename in filenames:
    data=data.replace(filename,filename+".png")
    # data=data.replace(filename+".png.png",filename+".png")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(data)
    # data=f.read()

print(filepath)