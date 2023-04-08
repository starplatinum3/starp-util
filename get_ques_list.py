
# D:\proj\job\questionList\questionList_https___www.nowcoder.com_exam_test_67762537_detail_pid=48310220&examPageSource=Company&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91.json

import json_util
json_path=rf"D:\proj\job\questionList\questionList_https___www.nowcoder.com_exam_test_67762537_detail_pid=48310220&examPageSource=Company&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91.json"
data=json_util.file_path_to_dict(json_path)
# data['questionList'][0]['question']
questionList=data['questionList']

# questionList=data['questionList'][0]['question']

question_title_list=[]
for question in questionList:
    question_title=question['question_title']
    question_title_list.append(question_title)
    # print(question['question_title'])
    # print(question['answer'])
    # print("")
print(question_title_list)