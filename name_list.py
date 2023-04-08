
# import strUtil

import string_util
# strUtil.str
table_name_list=['component', 'draw', 'eyesight_res', 'physical_test', 'question_draw', 't_chapter', 't_exam_paper', 't_exam_paper_answer', 't_exam_paper_question_customer_answer', 't_job_link', 't_message', 't_message_user', 't_question', 't_question_2', 't_subject', 't_task_exam', 't_task_exam_customer_answer', 't_text_content', 't_user', 't_user_event_log', 't_user_token', 'tenant', 'tenant_exam_paper']
# 计算机编程常见简化词转化成英语，请给出这个map
# cs_to_eng_map={
#     'res':'result',
# }

cs_to_eng_map = { 'res': 'result', 'ES': 'ECMAScript', 
                 'IDE': 'Integrated Development Environment', 'PC': 'Personal Computer', 
                 'PCB': 'Printed Circuit Board', 'PCI': 'Peripheral Component Interconnect',
                   'PCL': 'Printer Command Language', 'CMS': 'Content Management System', 
                   'CMYK': 'Cyan Magenta Yellow Black' }
def cs_to_eng(string):
    for k,v in cs_to_eng_map.items():
        string=string.replace(k,v)
    return string

def list_to_engs(table_name_list):
    for i in table_name_list:
        i=string_util.front_del_str(i,"t_")
        # i=i.replace('t_','')
        i=i.replace("_"," ")
        # i=i.replace("res","result")
        i=cs_to_eng(i)
        print(i)

eng_doc="""
component
draw
eyesight result
physical test
question draw
chapter
exam paper
exam paper answer
exam paper question customer answer
job link
message
message user
question
question 2
subject
task exam
task exam customer answer
text content
user
user event log
user token
tenant
tenant exam paper"""


eng_doc="""
Subsequent courses
Teaching unit
Course module
Total credit hours
"""


chinese_doc="""
组件
图画
视力测试结果
身体测试
问题图画配对
章节
试卷
试卷答案
试卷问题客户回答
工作链接
消息
消息用户
问题
问题2
科目
任务考试
任务考试客户回答
文本内容
用户
用户事件日志
用户令牌
租户
租户试卷"""

chinese_doc="""
后续课程
开课单位
课程模块
总学时
"""


chinese_doc="""
题型分布
考试时长
自查内容
持续改进措施
任课教师
审核内容
考试形式
教学改进情况
选课人数
难易分布
考核方式
"""
eng_doc="""
Question type distribution
Examination duration
Content of self inspection
Continuous improvement measures
teacher
Audit content
Examination form
Teaching improvement
Number of participants
Difficultly distributed
Assessment method"""

chinese_doc="""
学时分配
推荐教材及参考资料
讨论
热身活动：比手划脚
到课
课程考核及课程目标达成途径
报告
（三）课程目标与毕业要求的对应关系
课程思政元素及融入实施路径
课程内容、教学方法与课程目标的对应关系
（四）课程目标达成途径
作业
课程简介与课程目标
"""


chinese_doc="""
学时分配
推荐教材及参考资料
讨论
热身活动：比手划脚
到课
课程考核及课程目标达成途径
报告
课程目标与毕业要求的对应关系
课程思政元素及融入实施路径
课程内容、教学方法与课程目标的对应关系
课程目标达成途径
作业
课程简介与课程目标
"""

eng_doc="""
Credit hour allocation
Recommended textbooks and reference materials
discuss
Warm-up activity: Skimming
Arrive at class
Course Assessment and Ways to Achieve Course Objectives
report
Correspondence between course objectives and graduation requirements
Ideological and political elements of the curriculum and their integration into the implementation path
Correspondence between course content, teaching methods, and course objectives
Ways to achieve course objectives
task
Course Introduction and Objectives
"""



chinese_doc="""
成绩评定方法
实践环节及要求
课程介绍
绪论
实验环节及要求
浙大城市学院教学大纲
目标
课程内容、教学方法及学习要求
绪论
前沿课题
线下理论教学
学   分
总复习
课堂讲授、案例讲解、上机练习
"""

eng_doc="""
Score evaluation method
Practical links and requirements
Course Introduction
introduction
Experimental Procedures and Requirements
Teaching Syllabus of Zhejiang University City College
target
Course content, teaching methods, and learning requirements
introduction
Frontier topics
Offline theoretical teaching
Credits
Revision 
Classroom teaching, case explanation, and computer practice
"""


import list_util

# 期末考试

# '题型分布', '考试时长', '自查内容', '持续改进措施', '任课教师', '审核内容', '考试形式', '教学改进情况', '选课人数', '难易分布', '考核方式', 
# chinese_list=['教学内容','期末考试']
# chinese_list=['后续课程', '开课单位', '课程模块', '总学时', ]
# '期末考试', '教学内容', 
eng_list=list_util.to_lines(eng_doc)
chinese_list=list_util.to_lines(chinese_doc)

import string_util

# 中英文map 获取

for i in range(len(eng_list)):
    eng=eng_list[i]
    table_name=table_name_list[i]
    chinese=chinese_list[i]
    # print(f"ALTER TABLE {table_name} COMMENT '{chinese}';")
    underscore_lower=string_util.eng_to_underscore_lower(eng)
    print(f' "{chinese}": "{underscore_lower}",')