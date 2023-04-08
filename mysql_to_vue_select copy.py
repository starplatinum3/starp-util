# select TABLE_NAME,TABLE_TYPE,ENGINE,TABLE_ROWS,TABLE_COMMENT,CREATE_TIME,UPDATE_TIME, CHECK_TIME from information_schema.TABLES where TABLE_SCHEMA='t_shop' ;

"""
select TABLE_NAME,TABLE_TYPE,ENGINE,TABLE_ROWS,TABLE_COMMENT,CREATE_TIME,UPDATE_TIME, CHECK_TIME from information_schema.TABLES where TABLE_SCHEMA='t_shop' ;
"""


# table_name='t_exam_paper_answer'
# table_name='t_exam_paper'
table_name='product'


import pymysql

def get_all_tables(db_name):

    """

    获取数据库中的所有表

    """
    host='localhost'
    user='root'
    password="123456"
    db="public"
    # db="fastlink"
    # user='用户名',
    connection = pymysql.connect(host=host,
    user=user,

    password=password,

    db=db_name,
    # db=‘数据库名称’,
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

    # connection = pymysql.connect(host=host,

    # user='用户名',

    # password='密码',

    # db='数据库名称',
    # # db=‘数据库名称’,

    # charset='utf8',

    # cursorclass=pymysql.cursors.DictCursor)

    tables = []

    try:

        with connection.cursor() as cursor:

            # sql = '''SHOW TABLES''' # 同理 改成 '''SHOW DATABASES''' 即可获取所有数据库名称
            # sql =f"""
            # select * from information_schema.TABLES where TABLE_SCHEMA='{db_name}' ;

            # """
            # sql = f"""
            # select COLUMN_NAME from information_schema.COLUMNS where table_name = '{table_name}'
            # """
            # t_exam_paper_answer
            # table_name='t_exam_paper_answer'
            sql = f"""
            select * from information_schema.COLUMNS WHERE TABLE_SCHEMA = '{db_name}'  and table_name = '{table_name}'
            """

            cursor.execute(sql)

            table = cursor.fetchall() # 获取所有（输出是列表，列表中的每个元素是字典，字典的KEY是Tables_in_拼接数据库名称）

            for k in range(len(table)): # 提取表名

                # tables.append(table[k]['Tables_in_数据库名称'])
                tables.append(table[k])

    finally:

        connection.commit()

        connection.close()

    return tables

db_name="fastlink"
all_tables=get_all_tables(db_name=db_name)

# all_tables=get_all_tables(db_name='public')

# print(all_tables)
tables={
    "physicalTest":"physicalTest",
"physical_test":"physical_test",
"physical_test":"physical_test",
"tChapter":"tChapter",
"chapter":"chapter",
"t_chapter":"t_chapter",
"tExamPaper":"tExamPaper",
"exam_paper":"exam_paper",
"t_exam_paper":"t_exam_paper",
"tExamPaperAnswer":"tExamPaperAnswer",
"exam_paper_answer":"exam_paper_answer",
"t_exam_paper_answer":"t_exam_paper_answer",
"tExamPaperQuestionCustomerAnswer":"tExamPaperQuestionCustomerAnswer",
"exam_paper_question_customer_answer":"exam_paper_question_customer_answer",
"t_exam_paper_question_customer_answer":"t_exam_paper_question_customer_answer",
"tMessage":"tMessage",
"message":"message",
"t_message":"t_message",
"tMessageUser":"tMessageUser",
"message_user":"message_user",
"t_message_user":"t_message_user",
"tQuestion":"tQuestion",
"question":"question",
"t_question":"t_question",
"tQuestion2":"tQuestion2",
"question_2":"question_2",
"t_question_2":"t_question_2",
"tSubject":"tSubject",
"subject":"subject",
"t_subject":"t_subject",
"tTaskExam":"tTaskExam",
"task_exam":"task_exam",
"t_task_exam":"t_task_exam",
"tTaskExamCustomerAnswer":"tTaskExamCustomerAnswer",
"task_exam_customer_answer":"task_exam_customer_answer",
"t_task_exam_customer_answer":"t_task_exam_customer_answer",
"tTextContent":"tTextContent",
"text_content":"text_content",
"t_text_content":"t_text_content",
"tUser":"tUser",
"user":"user",
"t_user":"t_user",
"tUserEventLog":"tUserEventLog",
"user_event_log":"user_event_log",
"t_user_event_log":"t_user_event_log",
"tUserToken":"tUserToken",
"user_token":"user_token",
"t_user_token":"t_user_token",
"tenant":"tenant",
"tenant":"tenant",
"tenant":"tenant",
"tenantExamPaper":"tenantExamPaper",
"tenant_exam_paper":"tenant_exam_paper",
"tenant_exam_paper":"tenant_exam_paper",

}



"""
[{'Tables_in_public': 'component'}, {'Tables_in_public': 'draw'}, {'Tables_in_public': 'physical_test'}, {'Tables_in_public': '
question_draw'}, {'Tables_in_public': 't_chapter'}, {'Tables_in_public': 't_exam_paper'}, {'Tables_in_public': 't_exam_paper_an
swer'}, {'Tables_in_public': 't_exam_paper_question_customer_answer'}, {'Tables_in_public': 't_message'}, {'Tables_in_public':
't_message_user'}, {'Tables_in_public': 't_question'}, {'Tables_in_public': 't_question_2'}, {'Tables_in_public': 't_subject'},
 {'Tables_in_public': 't_task_exam'}, {'Tables_in_public': 't_task_exam_customer_answer'}, {'Tables_in_public': 't_text_content
'}, {'Tables_in_public': 't_user'}, {'Tables_in_public': 't_user_event_log'}, {'Tables_in_public': 't_user_token'}, {'Tables_in
_public': 'tenant'}, {'Tables_in_public': 'tenant_exam_paper'}]
"""

"""
D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\mysql_to_vue_select.py"
[{'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'component', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB',
'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 3, 'AVG_ROW_LENGTH': 5461, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'I
NDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 3, 'CREATE_TIME': datetime.datetime(2022, 12, 31, 20, 32, 42), 'UPDATE_TIME'
: None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''},
 {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'draw', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERS
ION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 5, 'AVG_ROW_LENGTH': 3276, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_
LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 7, 'CREATE_TIME': datetime.datetime(2022, 12, 31, 20, 31, 12), 'UPDATE_TIME': Non
e, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TA
BLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'physical_test', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', '
VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_ROW_LENGTH': 0, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX
_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': None, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 20, 48, 45), 'UPDATE_TIME':
 None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_0900_ai_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''
}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'question_draw', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'Inn
oDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_ROW_LENGTH': 0, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0,
 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 3, 'CREATE_TIME': datetime.datetime(2022, 12, 31, 20, 49, 18), 'UPDATE_TI
ME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_0900_ai_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT'
: ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_chapter', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'Inn
oDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 11, 'AVG_ROW_LENGTH': 1489, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH'
: 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 11, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 20, 48, 47), 'UPDA
TE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COM
MENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_exam_paper', 'TABLE_TYPE': 'BASE TABLE', 'ENGIN
E': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 85, 'AVG_ROW_LENGTH': 192, 'DATA_LENGTH': 16384, 'MAX_DATA_
LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 97, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 20, 48, 47)
, 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TA
BLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_exam_paper_answer', 'TABLE_TYPE': 'BASE
TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 199, 'AVG_ROW_LENGTH': 246, 'DATA_LENGTH': 49
152, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 211, 'CREATE_TIME': datetime.datetime(2022, 12,
 21, 20, 48, 47), 'UPDATE_TIME': datetime.datetime(2023, 1, 19, 13, 51, 57), 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_ge
neral_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TA
BLE_NAME': 't_exam_paper_question_customer_answer', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT'
: 'Dynamic', 'TABLE_ROWS': 402, 'AVG_ROW_LENGTH': 163, 'DATA_LENGTH': 65536, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FRE
E': 0, 'AUTO_INCREMENT': 451, 'CREATE_TIME': datetime.datetime(2023, 1, 3, 20, 20, 49), 'UPDATE_TIME': datetime.datetime(2023,
1, 19, 13, 51, 57), 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE
_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_message', 'TABLE_TYPE': 'BASE TABLE', 'ENGI
NE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 5, 'AVG_ROW_LENGTH': 3276, 'DATA_LENGTH': 16384, 'MAX_DATA
_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 6, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 20, 48, 47)
, 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TA
BLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_message_user', 'TABLE_TYPE': 'BASE TABLE
', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 14, 'AVG_ROW_LENGTH': 1170, 'DATA_LENGTH': 16384,
'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 15, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 2
0, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS
': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_question', 'TABLE_TYPE': 'BASE
 TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 77, 'AVG_ROW_LENGTH': 212, 'DATA_LENGTH': 16
384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 131, 'CREATE_TIME': datetime.datetime(2023, 1,
16, 21, 28, 26), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OP
TIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_question_2', 'TABLE_TYPE'
: 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 33, 'AVG_ROW_LENGTH': 496, 'DATA_LENG
TH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 50, 'CREATE_TIME': datetime.datetime(202
2, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CR
EATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_subject', 'TABLE_T
YPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 13, 'AVG_ROW_LENGTH': 1260, 'DATA
_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 16, 'CREATE_TIME': datetime.datetim
e(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None
, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_task_exam', '
TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_ROW_LENGTH': 0, 'D
ATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 2, 'CREATE_TIME': datetime.datet
ime(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': No
ne, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_task_exam_c
ustomer_answer', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_
ROW_LENGTH': 0, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 1, 'CREATE_TIM
E': datetime.datetime(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_c
i', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAM
E': 't_text_content', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 379
, 'AVG_ROW_LENGTH': 345, 'DATA_LENGTH': 131072, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 16384, 'DATA_FREE': 0, 'AUTO_INCREMENT':
461, 'CREATE_TIME': datetime.datetime(2023, 1, 17, 22, 28, 51), 'UPDATE_TIME': datetime.datetime(2023, 1, 19, 11, 3, 40), 'CHEC
K_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_C
ATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_user', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10
, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 19, 'AVG_ROW_LENGTH': 862, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH':
 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 21, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 23, 6, 42), 'UPDATE_TIME': None, 'CHEC
K_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_C
ATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_user_event_log', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VE
RSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 527, 'AVG_ROW_LENGTH': 155, 'DATA_LENGTH': 81920, 'MAX_DATA_LENGTH': 0, 'IND
EX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 792, 'CREATE_TIME': datetime.datetime(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME'
: datetime.datetime(2023, 1, 19, 13, 51, 57), 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': None, 'C
REATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 't_user_token', 'TAB
LE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 19, 'AVG_ROW_LENGTH': 862, 'D
ATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 23, 'CREATE_TIME': datetime.date
time(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': N
one, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'tenant', 'TA
BLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_ROW_LENGTH': 0, 'DAT
A_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': None, 'CREATE_TIME': datetime.date
time(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'CHECKSUM': N
one, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}, {'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'tenant_exam_
paper', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 0, 'AVG_ROW_LENGT
H': 0, 'DATA_LENGTH': 16384, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': None, 'CREATE_TIME': da
tetime.datetime(2022, 12, 21, 20, 48, 47), 'UPDATE_TIME': None, 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_general_ci', 'C
HECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}]
"""

# print("all_tables[0]")
# print(all_tables[0])
print("table_name")
csharp_type_map={
    'int':'int?',
    'varchar':'string',
    'datetime':'DateTime?',
    'text':'string',
    'decimal':'decimal?',
    'bigint':'long?',
    'tinyint':'bool?'

}
def to_csharp_type(DATA_TYPE):
    if DATA_TYPE in csharp_type_map:
        return csharp_type_map[DATA_TYPE]
    return 'string'
  


import string_util
print(table_name)

try:
    print()
except NameError as e:
    print(e)

def genElInput():

    for col_info in all_tables:
        COLUMN_NAME=col_info['COLUMN_NAME']
        # to_lower_camel_case()
        col_info['lower_camel_case_COLUMN_NAME']=string_util.to_lower_camel_case(COLUMN_NAME)
        col_info['upper_camel_case_COLUMN_NAME']=string_util.to_upper_camel_case(COLUMN_NAME)
        lower_camel_case_COLUMN_NAME=col_info['lower_camel_case_COLUMN_NAME']
        # input_div=f'<el-input v-model="query.{COLUMN_NAME}"></el-input>'
        # queryParam
        # query
        
        COLUMN_COMMENT=col_info['COLUMN_COMMENT']
        COLUMN_COMMENT_show=COLUMN_COMMENT if COLUMN_COMMENT else COLUMN_NAME
        input_div=f"""
        
         <el-form-item label="{COLUMN_COMMENT_show}">
          <el-input v-model="queryParam.{lower_camel_case_COLUMN_NAME}" clearable  placeholder="{COLUMN_COMMENT_show}"></el-input>
        </el-form-item>
        """
        # input_div=f'{lower_camel_case_COLUMN_NAME}  <el-input v-model="queryParam.{lower_camel_case_COLUMN_NAME}"></el-input>'
        print(input_div)
        # tables.t
"""
{'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'public', 'TABLE_NAME': 'component', 'COLUMN_NAME': 'id', 'ORDINAL_POSITION': 1, 'COLU
MN_DEFAULT': None, 'IS_NULLABLE': 'NO', 'DATA_TYPE': 'int', 'CHARACTER_MAXIMUM_LENGTH': None, 'CHARACTER_OCTET_LENGTH': None, '
NUMERIC_PRECISION': 10, 'NUMERIC_SCALE': 0, 'DATETIME_PRECISION': None, 'CHARACTER_SET_NAME': None, 'COLLATION_NAME': None, 'CO
LUMN_TYPE': 'int', 'COLUMN_KEY': 'PRI', 'EXTRA': 'auto_increment', 'PRIVILEGES': 'select,insert,update,references', 'COLUMN_COMMENT': '编号', 'GENERATION_EXPRESSION': '', 'SRS_ID': None}
"""

def genCSharpClass():
    print(all_tables)
    # table_name
    table_name_class_name=string_util.to_upper_camel_case(table_name)
    # print(f"public class Blog {")
    row_val_list=[]
    for col_info in all_tables:
        COLUMN_NAME=col_info['COLUMN_NAME']
        # to_lower_camel_case()
        col_info['lower_camel_case_COLUMN_NAME']=string_util.to_lower_camel_case(COLUMN_NAME)
        col_info['upper_camel_case_COLUMN_NAME']=string_util.to_upper_camel_case(COLUMN_NAME)
        lower_camel_case_COLUMN_NAME=col_info['lower_camel_case_COLUMN_NAME']
        # input_div=f'<el-input v-model="query.{COLUMN_NAME}"></el-input>'
        # queryParam
        # query
        
        COLUMN_COMMENT=col_info['COLUMN_COMMENT']
        COLUMN_COMMENT_show=COLUMN_COMMENT if COLUMN_COMMENT else COLUMN_NAME
        # public class Blog {
        #     [Column(IsIdentity = true, IsPrimary = true)]
        #     public int BlogId { get; set; }
        #     public string Url { get; set; }
        #     public int Rating { get; set; }
        # }
        DATA_TYPE=col_info['DATA_TYPE']
        csharp_type=to_csharp_type(DATA_TYPE)
        # input_div= "public int {COLUMN_COMMENT} { get; set; }".replace("{COLUMN_COMMENT}",COLUMN_COMMENT)
        input_div= "public {csharp_type} {COLUMN_NAME} { get; set; }".replace("{COLUMN_NAME}",COLUMN_NAME)\
        .replace("{DATA_TYPE}",DATA_TYPE)\
        .replace("{csharp_type}",csharp_type)\
        # input_div=f"""
        #  public int COLUMN_COMMENT { get; set; }
        row_val_list.append(input_div)
        # """
        # input_div=f'{lower_camel_case_COLUMN_NAME}  <el-input v-model="queryParam.{lower_camel_case_COLUMN_NAME}"></el-input>'
        # print(input_div)
        # tables.t
    # row_val_list.join()
    field_rows="\n".join(row_val_list)
    class_file_tpl="""
        using FreeSql.DataAnnotations;
        using System;

        public class {table_name_class_name} {
            [Column(IsIdentity = true, IsPrimary = true)]
            {field_rows}
        }"""
    return class_file_tpl.replace("{table_name_class_name}",table_name_class_name).\
        replace("{field_rows}",field_rows)

# def toFieldMysqlMapEntity(col_info):

def toFieldMysqlMapEntity(col_info):
    DATA_TYPE=col_info['DATA_TYPE']
    COLUMN_NAME=col_info['COLUMN_NAME']
    # line.{COLUMN_NAME} = {COLUMN_NAME};
    if DATA_TYPE=='int':
        return f"""
        int {COLUMN_NAME} = 0;
        int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});
        """
    if DATA_TYPE=='datetime':
        return f"""
        DateTime {COLUMN_NAME} = DateTime.Now;
        DateTime.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='decimal':
        return f"""
        decimal {COLUMN_NAME} = 0;
        decimal.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='varchar':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='text':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='tinyint':
        return f"""
        int {COLUMN_NAME} = 0;
        int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='bigint':
        return f"""
        long {COLUMN_NAME} = 0;
        long.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='float':
        return f"""
        float {COLUMN_NAME} = 0;
        float.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='double':
        return f"""
        double {COLUMN_NAME} = 0;
        double.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='bit':
        return f"""
        bool {COLUMN_NAME} = false;
        bool.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='char':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='date':
        return f"""
        DateTime {COLUMN_NAME} = DateTime.Now;
        DateTime.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='time':
        return f"""
        TimeSpan {COLUMN_NAME} = new TimeSpan();
        TimeSpan.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='timestamp':
        return f"""
        DateTime {COLUMN_NAME} = DateTime.Now;
        DateTime.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='year':
        return f"""
        int {COLUMN_NAME} = 0;
        int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='mediumint':
        return f"""
        int {COLUMN_NAME} = 0;
        int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='smallint':
        return f"""
        int {COLUMN_NAME} = 0;
        int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});"""
    if DATA_TYPE=='tinytext':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='mediumtext':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='longtext':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='enum':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='set':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='blob':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='mediumblob':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='longblob':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='varbinary':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='binary':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='geometry':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='point':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    if DATA_TYPE=='linestring':
        return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""
    return f"""
        string {COLUMN_NAME} = reader["{COLUMN_NAME}"].ToString();"""

#     """
#     int id = 0;
#    int.TryParse(reader["id"].ToString(), out id);"""

def genMysqlMapToEntity():
    print(all_tables)
    # table_name
    table_name_class_name=string_util.to_upper_camel_case(table_name)
    # print(f"public class Blog {")
    row_val_list=[]
    for col_info in all_tables:
        COLUMN_NAME=col_info['COLUMN_NAME']
        # to_lower_camel_case()
        col_info['lower_camel_case_COLUMN_NAME']=string_util.to_lower_camel_case(COLUMN_NAME)
        col_info['upper_camel_case_COLUMN_NAME']=string_util.to_upper_camel_case(COLUMN_NAME)
        lower_camel_case_COLUMN_NAME=col_info['lower_camel_case_COLUMN_NAME']
        # input_div=f'<el-input v-model="query.{COLUMN_NAME}"></el-input>'
        # queryParam
        # query
        
        COLUMN_COMMENT=col_info['COLUMN_COMMENT']
        # DATA_TYPE=col_info['DATA_TYPE']
        COLUMN_COMMENT_show=COLUMN_COMMENT if COLUMN_COMMENT else COLUMN_NAME
        # if DATA_TYPE:
        # public class Blog {
        #     [Column(IsIdentity = true, IsPrimary = true)]
        #     public int BlogId { get; set; }
        #     public string Url { get; set; }
        #     public int Rating { get; set; }
        # }
        # DATA_TYPE
        FieldMysqlMapEntity=toFieldMysqlMapEntity(col_info)
        # DATA_TYPE=col_info['DATA_TYPE']
        # COLUMN_NAME=col_info['COLUMN_NAME']
        
        # if DATA_TYPE=='int':
        #     return f"""
        #     int {COLUMN_NAME} = 0;
        #     int.TryParse(reader["{COLUMN_NAME}"].ToString(), out {COLUMN_NAME});
        #     line.{COLUMN_NAME} = {COLUMN_NAME};
        #     """
        # line.{COLUMN_NAME} = {COLUMN_NAME};
        # input_div= "public int {COLUMN_COMMENT} { get; set; }".replace("{COLUMN_COMMENT}",COLUMN_COMMENT)
        # input_div= "public int {COLUMN_NAME} { get; set; }".replace("{COLUMN_NAME}",COLUMN_NAME)
        # input_div=f"""
        #  public int COLUMN_COMMENT { get; set; }
        row_val_list.append(FieldMysqlMapEntity)
        row_val_list.append(f"line.{COLUMN_NAME} = {COLUMN_NAME};")
        # row_val_list.append(input_div)
        # """
        # input_div=f'{lower_camel_case_COLUMN_NAME}  <el-input v-model="queryParam.{lower_camel_case_COLUMN_NAME}"></el-input>'
        # print(input_div)
        # tables.t
    # row_val_list.join()
    field_rows="\n".join(row_val_list)
    class_file_tpl="""
        using FreeSql.DataAnnotations;
        using System;

        public class {table_name_class_name} {
            [Column(IsIdentity = true, IsPrimary = true)]
            {field_rows}
        }"""
    return class_file_tpl.replace("{table_name_class_name}",table_name_class_name).\
        replace("{field_rows}",field_rows)


def genCreate():
    print(all_tables)
    # table_name
    table_name_class_name=string_util.to_upper_camel_case(table_name)
    # print(f"public class Blog {")
    row_val_list=[]
    COLUMN_NAME_list=[]
    COLUMN_NAME_at_list=[]
    AddWithValue_row_list=[]
    for col_info in all_tables:
        COLUMN_NAME=col_info['COLUMN_NAME']
        COLUMN_NAME_list.append(COLUMN_NAME)
        COLUMN_NAME_at_list.append(f"@{COLUMN_NAME}")
        # to_lower_camel_case()
        col_info['lower_camel_case_COLUMN_NAME']=string_util.to_lower_camel_case(COLUMN_NAME)
        col_info['upper_camel_case_COLUMN_NAME']=string_util.to_upper_camel_case(COLUMN_NAME)
        lower_camel_case_COLUMN_NAME=col_info['lower_camel_case_COLUMN_NAME']
        # input_div=f'<el-input v-model="query.{COLUMN_NAME}"></el-input>'
        # queryParam
        # query
        AddWithValue_row=f'com.Parameters.AddWithValue("@{COLUMN_NAME}", line.{COLUMN_NAME});'
        AddWithValue_row_list.append(AddWithValue_row)
        
        COLUMN_COMMENT=col_info['COLUMN_COMMENT']
        # DATA_TYPE=col_info['DATA_TYPE']
        COLUMN_COMMENT_show=COLUMN_COMMENT if COLUMN_COMMENT else COLUMN_NAME
        # if DATA_TYPE:
        # public class Blog {
        #     [Column(IsIdentity = true, IsPrimary = true)]
        #     public int BlogId { get; set; }
        #     public string Url { get; set; }
        #     public int Rating { get; set; }
        # }
        # DATA_TYPE
        FieldMysqlMapEntity=toFieldMysqlMapEntity(col_info)

        row_val_list.append(FieldMysqlMapEntity)
        row_val_list.append(f"line.{COLUMN_NAME} = {COLUMN_NAME};")

    field_rows="\n".join(row_val_list)
    

    COLUMN_NAMEs=", ".join(COLUMN_NAME_list)
    COLUMN_NAME_at_list_str=", ".join(COLUMN_NAME_at_list)
    AddWithValue_row_list_str="\n".join(AddWithValue_row_list)
    class_file_tpl="""
        //create
        [HttpPost]
        [Route("api/{table_name}")]
        // POST: api/{table_name}
        public void Post([FromBody]{table_name_class_name} line)
        {
            using (MySqlConnection conn = this.GetConnection())
            {
                using (MySqlCommand com = new MySqlCommand())
                {
                    com.Connection = conn;
                    com.CommandText = "insert into {table_name}({COLUMN_NAMEs}) values ({COLUMN_NAME_at_list_str}) ";
                    {AddWithValue_row_list_str}
                    com.ExecuteNonQuery();
                }
            }
        }
        """
    return class_file_tpl.replace("{table_name_class_name}",table_name_class_name).\
        replace("{field_rows}",field_rows)\
        .replace("{COLUMN_NAMEs}",COLUMN_NAMEs)\
        .replace("{COLUMN_NAME_at_list_str}",COLUMN_NAME_at_list_str)\
        .replace("{AddWithValue_row_list_str}",AddWithValue_row_list_str)\
        .replace("{table_name}",table_name)\




def genPut():
    print(all_tables)
    # table_name
    table_name_class_name=string_util.to_upper_camel_case(table_name)
    # print(f"public class Blog {")
    row_val_list=[]
    COLUMN_NAME_list=[]
    COLUMN_NAME_at_list=[]
    AddWithValue_row_list=[]
    COLUMN_NAME_update_set_list=[]
    if_not_null_select_list=[]
    for col_info in all_tables:
        COLUMN_NAME=col_info['COLUMN_NAME']
        COLUMN_NAME_list.append(COLUMN_NAME)
        COLUMN_NAME_at_list.append(f"@{COLUMN_NAME}")
        if COLUMN_NAME!="id":
            COLUMN_NAME_update_set_list.append(f"{COLUMN_NAME} = @{COLUMN_NAME}")
        # birthday=@birthday
        # to_lower_camel_case()
        
        if_tpl="""
        if (postData.{COLUMN_NAME} != null)
        {
            values.Add($" {COLUMN_NAME} = @{COLUMN_NAME} ");
            com.Parameters.AddWithValue("@{COLUMN_NAME}", postData.{COLUMN_NAME});
        }
        """
        if_not_null_select=if_tpl.replace("{COLUMN_NAME}",COLUMN_NAME)
        if_not_null_select_list.append(if_not_null_select)
        col_info['lower_camel_case_COLUMN_NAME']=string_util.to_lower_camel_case(COLUMN_NAME)
        col_info['upper_camel_case_COLUMN_NAME']=string_util.to_upper_camel_case(COLUMN_NAME)
        lower_camel_case_COLUMN_NAME=col_info['lower_camel_case_COLUMN_NAME']
        # input_div=f'<el-input v-model="query.{COLUMN_NAME}"></el-input>'
        # queryParam
        # query
        AddWithValue_row=f'com.Parameters.AddWithValue("@{COLUMN_NAME}", line.{COLUMN_NAME});'
        AddWithValue_row_list.append(AddWithValue_row)
        
        COLUMN_COMMENT=col_info['COLUMN_COMMENT']
        # DATA_TYPE=col_info['DATA_TYPE']
        COLUMN_COMMENT_show=COLUMN_COMMENT if COLUMN_COMMENT else COLUMN_NAME
        # if DATA_TYPE:
        # public class Blog {
        #     [Column(IsIdentity = true, IsPrimary = true)]
        #     public int BlogId { get; set; }
        #     public string Url { get; set; }
        #     public int Rating { get; set; }
        # }
        # DATA_TYPE
        FieldMysqlMapEntity=toFieldMysqlMapEntity(col_info)

        row_val_list.append(FieldMysqlMapEntity)
        row_val_list.append(f"line.{COLUMN_NAME} = {COLUMN_NAME};")

    field_rows="\n".join(row_val_list)
    

    COLUMN_NAMEs=", ".join(COLUMN_NAME_list)
    COLUMN_NAME_at_list_str=", ".join(COLUMN_NAME_at_list)
    AddWithValue_row_list_str="\n".join(AddWithValue_row_list)
    COLUMN_NAME_update_set_list_str=", ".join(COLUMN_NAME_update_set_list)
    if_not_null_select_list_str="\n".join(if_not_null_select_list)
    class_file_tpl="""
        [HttpPost]
        [Route("api/{table_name}/put")]
        // PUT: api/{table_name}/5
        public object Put( [FromBody] {table_name_class_name} line)
        {
            using (MySqlConnection conn = this.GetConnection())
            {
                using (MySqlCommand com = new MySqlCommand())
                {
                    com.Connection = conn;
                    com.CommandText = "update {table_name} set {COLUMN_NAME_update_set_list_str} where id=@id ";
                    {AddWithValue_row_list_str}
                    com.ExecuteNonQuery();
                }
            }
             return ReturnT.Ok("ok");
        }

        [HttpPost]
        [Route("api/{table_name}/delete")]
        // DELETE: api/{table_name}/5
        public object Delete([FromBody] {table_name_class_name} line)
        {
            using (MySqlConnection conn = this.GetConnection())
            {
                using (MySqlCommand com = new MySqlCommand())
                {
                    com.Connection = conn;
                    com.CommandText = "delete from {table_name} where id=@id ";
                    com.Parameters.AddWithValue("@id", line.id);
                    com.ExecuteNonQuery();
                }
            }
             return ReturnT.Ok("ok");
        }


         [HttpPost]
        [Route("api/{table_name}")]
        // GET api/{table_name}
        public object selectPage([FromBody] {table_name_class_name}  postData,int pageIndex,int pageSize)
        {
            List<{table_name_class_name}> list = new List<{table_name_class_name}>();
            using (MySqlConnection conn = this.GetConnection())
            {
                using (MySqlCommand com = new MySqlCommand())
                {
                    com.Connection = conn;
                    com.CommandText = "select * from {table_name} where ";
                    MySqlDataReader reader = com.ExecuteReader();
                    while (reader.Read())
                    {
                        {table_name_class_name} line   = new {table_name_class_name}();
                       {field_rows}
                    }
                }
            }
            return list.ToArray();
        }

        [HttpPost]
           [Route("api/{table_name}/selectPage")]
        // GET api/{table_name}
       public object selectPage([FromBody] {table_name_class_name}  postData,int pageIndex,int pageSize)
        {
             List<{table_name_class_name}> list = new List<{table_name_class_name}>();
            using (MySqlConnection conn = this.GetConnection())
            {
                using (MySqlCommand com = new MySqlCommand())
                {
                    com.Connection = conn;
                    string sql = "select * from {table_name}   ";

                    List<string> values = new List<string>();
                    {if_not_null_select_list_str}
                  
                  
                    string whereCondition = string.Join(" \\n and ", values);
           
                    if (values.Count > 0)
                    {
                        sql +="  where  "+ whereCondition;
                    }

                    com.CommandText = sql;
                   
                    MySqlDataReader reader = com.ExecuteReader();
                    while (reader.Read())
                    {
                         {table_name_class_name} line   = new {table_name_class_name}(); 
                       {field_rows}
                        list.Add(line);
                    }
                }
            }
            return list.ToArray();
        }

        """
    return class_file_tpl.replace("{table_name_class_name}",table_name_class_name).\
        replace("{field_rows}",field_rows)\
        .replace("{COLUMN_NAMEs}",COLUMN_NAMEs)\
        .replace("{COLUMN_NAME_at_list_str}",COLUMN_NAME_at_list_str)\
        .replace("{AddWithValue_row_list_str}",AddWithValue_row_list_str)\
        .replace("{table_name}",table_name)\
        .replace("{COLUMN_NAME_update_set_list_str}",COLUMN_NAME_update_set_list_str)\
        .replace("{if_not_null_select_list_str}",if_not_null_select_list_str)\
        

# COLUMN_NAME

# genElInput()
   
# CSharpClass=genCSharpClass()

# print(CSharpClass)
"""

  public class Product {
            [Column(IsIdentity = true, IsPrimary = true)]
            public int create_time { get; set; }
public int id { get; set; }
public int name { get; set; }
public int product_code { get; set; }
public int specification { get; set; }
        }
        """

# D:\codeGen\genCSharp
genOutDir=r"D:\codeGen\genCSharp"
# res=genMysqlMapToEntity()
# res=genCSharpClass()
# res=genCreate()
# # genName="genCSharpClass"
# genName="genCreate"

res=genPut()
genName="genPut"

print(res)

import time_util
now_time_str=time_util.get_now_time_str()

# import
# def get_now_time_str():
#     now_time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#     return now_time_str


# get_now_time_str=get_now_time()


outFileName=f"{genOutDir}/{table_name}_{genName}_{now_time_str}.cs"
print("outFileName")
print(outFileName)

with open(outFileName, "w") as f:
    f.write(res)

# with open(f"{table_name}_genMysqlMapToEntity.cs", "w") as f:
#     f.write(res)