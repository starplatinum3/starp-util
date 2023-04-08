
code_path=rf"D:\proj\python\my_util_py_pub\code.java"

# import 
with open(code_path,'r',encoding='utf-8') as f:
    code=f.read()
code=code.replace(';import',';\nimport ')

code=code.replace(';public',';\n  public ')

code=code.replace('{public','{\n  public ')

code=code.replace('packagecom','package  com')

code=code.replace('voidmain','void main')
code=code.replace('class','class ')
print(code)

with open('CodeCLean.java','w',encoding='utf-8') as f:
    f.write(code)