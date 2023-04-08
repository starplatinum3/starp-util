api = "select_information_schema_columns";

with open("postJava.java","r") as f:
    tempalte=f.read()
    postJavaCode=tempalte.replace("#doName#",api)

print(postJavaCode)