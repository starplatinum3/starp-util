
# eng_str="""
# Student ID
# full name
# Gender
# college
# Professional class
# Total score
# Grade
# Student status"""

# chinese_col_str="""
# 学号	姓名	性别	学院	专业班级	总分	等级	学籍状态
# """

# chinese_col_str=chinese_col_str.strip()

# chinese_cols=chinese_col_str.split("\t")

# for col in chinese_cols:
#     print(col)

# eng_str=eng_str.strip()

# engs=eng_str.split("\n")
# 体测成绩 体育 体育成绩 体育成绩
# physical_test results
# Physical test results
def make_col(eng):
    # lo 
    # python lower 
    eng=eng.lower()
    col=eng.replace(" ","_")
    return  col

# mysql  create 
#  

# CREATE TABLE `physical_test` (
#   `student_id` int DEFAULT NULL,
#   `full_name` varchar(255) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

def type_like_in_list(col_name,little_key_word_type_list):
    for key_word in little_key_word_type_list:
        if key_word in col_name:
            return True
    return False

def get_col_ddl_row_map(col):
    """
    ddl_row_map=get_col_ddl_row_map("student_id")
    print(ddl_row_map)
    # "student_id"
    # {'col': 'student_id', 'type': 'int', 'col_ddl_row': '`student_id` int DEFAULT NULL', 'DEFAULT': 'NULL'}
    # """
    int_type_list=["id",]
    double_type_list=["grade"]
    varchar_type_list=["name"]
    res={
        "comment":"",
    }
    if type_like_in_list(col,int_type_list):
        col_ddl_row= f"`{col}` int DEFAULT NULL"
        return {
            "col":col,
            "type":"int",
            "col_ddl_row":col_ddl_row,
            "DEFAULT":"NULL"
        }
    if type_like_in_list(col,double_type_list):
        return {
            "col":col,
            "type":"double",
            "DEFAULT":"NULL"
        }
    # if "id" in col or "grade" in col:
    #     col_ddl_row= f"`{col}` int DEFAULT NULL"
    #     return {
    #         "col":col,
    #         "type":"int",
    #         "col_ddl_row":col_ddl_row,
    #         "DEFAULT":"NULL"
    #     }
    # if col in 
    if "name" in col:
        return {
            "col":col,
            "type":"varchar(255)",
            # "col_ddl_row":col_ddl_row,
            "DEFAULT":"NULL"
        }
    if "status" in col:
        return {
            "col":col,
            "type":"varchar(30)",
            "DEFAULT":"NULL"
        }
    if "time" in col or "date" in col:
        return {
            "col":col,
            "type":"datetime",
            "DEFAULT":"NULL"
        }
    if "gender" in col or "sex" in col:
        return {
            "col":col,
            "type":"varchar(10)",
            "DEFAULT":"NULL"
        }
    # gender
    return {
            "col":col,
            "type":"varchar(255)",
            # "col_ddl_row":col_ddl_row,
            "DEFAULT":"NULL"
        }
    # col_ddl_row=f"`{col}` varchar(255) DEFAULT NULL"
    # return  col_ddl_row

def get_ddl_row_by_map(map):
    # COMMENT '试卷名称'
    #  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
    col_ddl_row=f"`{map['col']}` {map['type']}  DEFAULT {map['DEFAULT']} COMMENT  '{map['comment']}' "
    return col_ddl_row


# ddl_row_list=[]

def add_comment(map,comment):
    map["comment"]=comment
    return map

def get_ddl_row_list(engs,chinese_cols):
    ddl_row_list=[]
    idx=0
    for eng in engs:
        col=make_col(eng)
        print(col)
        col_ddl_row_map=get_col_ddl_row_map(col)
        col_ddl_row_map=add_comment(col_ddl_row_map,chinese_cols[idx])
        idx+=1
        ddl_row_by_map=get_ddl_row_by_map(col_ddl_row_map)
        
        ddl_row_list.append(ddl_row_by_map)
    return ddl_row_list

def get_ddl_rows(df):
    ddl_row_list = get_ddl_row_list(df.columns, df.columns)

    ddl_rows = ",\n".join(ddl_row_list)
    return ddl_rows
# idx=0
# for eng in engs:
#     col=make_col(eng)
#     print(col)
#     col_ddl_row_map=get_col_ddl_row_map(col)
#     col_ddl_row_map=add_comment(col_ddl_row_map,chinese_cols[idx])
#     idx+=1
#     ddl_row_by_map=get_ddl_row_by_map(col_ddl_row_map)
    
#     ddl_row_list.append(ddl_row_by_map)


# table_name="physical_test"

# ddl_row_list_str=",\n".join(ddl_row_list)
# # ddl_row_list.jo 
# dll_create=f"""
# DROP TABLE IF EXISTS `{table_name}`;

# CREATE TABLE `{table_name}` (
#  {ddl_row_list_str}
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# """

# print(dll_create)
# “DROP TABLE [IF EXISTS] 表名列表”;

# CREATE TABLE `physical_test` (
#  `student_id` int DEFAULT NULL,
# `full_name` varchar(255) DEFAULT NULL,
# `gender` varchar(10) DEFAULT NULL,
# `college` varchar(255) DEFAULT NULL,
# `professional_class` varchar(255) DEFAULT NULL,
# `total_score` varchar(255) DEFAULT NULL,
# `grade` double DEFAULT NULL,
# `student_status` varchar(30) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

if __name__=="__main__":
    pass 
    ddl_row_map=get_col_ddl_row_map("student_id")
    print(ddl_row_map)
    # "student_id"
    # {'col': 'student_id', 'type': 'int', 'col_ddl_row': '`student_id` int DEFAULT NULL', 'DEFAULT': 'NULL'}