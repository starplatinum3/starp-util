funzhi_sentence="""
 this.score = question.getScore();
//        this.difficulty = question.getDifficult();
        this.difficulty = question.getDifficult() * 1.0 / 5;
        this.type = question.getQuestionType();
//    this.=question.getQuestionType();
        this.id = question.getId();
//        this.id = question.getId();
        this.quesContent = question.getQuesContent();
        this.questionType = question.getQuestionType();
        this.subjectId = question.getSubjectId();
        this.score = question.getScore();
        this.gradeLevel = question.getGradeLevel();
        this.difficult = question.getDifficult();
        this.correct = question.getCorrect();
        this.infoTextContentId = question.getInfoTextContentId();
        this.createUser = question.getCreateUser();
        this.videoLink = question.getVideoLink();
        this.status = question.getStatus();
//        this.createTime = question.getCreateTime();
        this.deleted = question.getDeleted();
        this.analyze = question.getAnalyze();
        this.title = question.getTitle();
        this.items = question.getItems();"""

funzhi_sentence=funzhi_sentence.strip()

lines=funzhi_sentence.split('\n')
import re
filedList=[]
import listUtil
# listUtil.list_same
# python list 找相同的 
for line in lines:
    # print(line)
    line:str
    line=line.strip()
    if line.startswith('//'):
        continue
    # python 正则 获取 this .
    # searchObj =re.search(r'^this\.(.*)$=',line)
    searchObj =re.search(r'this\.(.*) =',line)
    # searchObj.group().print 
    filed=searchObj.group(1)
    print(searchObj.group(1))
    filedList.append(filed)

# find_same_in_one
# listUtil.find_same(filedList,filedList)
filedListSame=listUtil.find_same_in_one(filedList)
print(filedListSame)
