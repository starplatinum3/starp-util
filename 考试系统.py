


# str="""
#  随着社会经济的发展和网络技术的全面普及，网络化培训教育成为教育改
# 革的一个重要特征，并对教育行业的发展形成了新的推动力。传统的线下培训
# 和考试模式因其从考场组织、审定编制、试卷发放、评判归档等各个环节需要
# 人工的干预，耗费时间成本、场地成本和人工成本较高，且难以保证其客观性
# 和公正性，己不能完全满足企业发展的要求。通过Ir}te}}t技术实现线上培训和
# 考试，可以从问卷发放、评判等环节实现自动化，有效避免疫情期间线下考试
# 的聚集性风险，屏蔽了人工干预的可能性，具有线下考试无法比拟的优点。因
# 此企业数字化己经成为企业培训未来的发展趋势，从传统E一learning到移动学
# 习APP软件，数字化培训平台已成为企业培训的重要工具。
# """

# from unicodedata import name


str="""
    2020年中国移动通信集团大会上，董事长杨杰指出:“渠道工作需加快转
型升级步伐，打造线上线下结合、自有社会并重、传统新型协同的渠道格局，
建设好智慧中台，有效支撑内外部的运营管理发展”。通过对200多家核心渠道
走访调研，发现存在的主要问题是培训不及时、培训听不懂，缺少场景化话术，
网格经理再培训能力欠缺，业务掌握熟练度没有达到预期，对一些新推出的资
费政策无法做到熟练于心。因此为提升全渠道能力，跟上市场发展瞬息万变的
节奏，需要围绕“卜N+X”工作体系，纵向搭建全渠道培训体系。
"""

str="""

    近十年来，国内外陆续有公司和学者开展教学答题系统的研究，并开发出了各
种可行的教学答题产品。由于国外的信息技术比我国先进，国外的研究要更超前一
些。以谷歌公司于2014年发布的“Google Classroom(谷歌课堂)”[32]为代表，简
化了分配作业的教学界面，同时，也简化了各类公告、邮件和推送通知的界面，使
教师用于布置和评定作业的时间得以降低[[33]，节省的时间被用于了与学生沟通，确
保了教学质量。此外，谷歌课堂给予了学生一个更好地协作学习的平台[[34]，学生和
老师都能通过该系统上传文档资料，其他人可以留言讨论，通过合作讨论的方式，
有效提高了作业质量。
"""

str="""
自动组卷和自动阅卷部分的设计与实现是考试系统的关键点。组卷部分使用基于基本遗传算法的组卷模型，结合实际需求对组卷目标、试卷约束条件和试题属性进行分析，建
立组卷问题求解的数学模型，并针对基本遗传算法的各个阶段给出了具体设
计实现过程和个性化的改进方法;自动阅卷部分模拟人工评阅过程，综合考
虑语义信息和语句内部结构信息对文本的影响，采用改进的基于《同义词词
林》词语语义相似度和词序相似度融合的阅卷模型，并通过统计回归分析的
方式对词语相似度和词序相似度进行融合，得到文本的综合相似度，进而预
估考生得分。

"""

str="""

    从图中可以看出，本系统与教师相关的系统用例图主要有的功能为:日志信
息的查看、考试题目的管理、考试考场的管理、考试科目的发布、考卷的管理、
考试成绩的管理、考试前的专家答疑以及考试的新闻管理，同时对于信息化的系
统还有的就是各种数据的增删改查，主要包括的功能有:用户的增删改查、年级
信息的增删改查、班级的增删改查以及用户授权等等这一系列的后台数据的管
理。
    从图中可以看出，本系统与学生相关的系统用例图主要有的功能为:系统的
登陆、考试的完成以及成绩的查询，在线考试系统主要是提供考试的，所以学员
考试模块是系统的大部分模块，也是开发过程中代码量最大的模块。同时对于学
员本系统也提供了日志查询功能，主要实现的功能是学生考试过程中考试记录的
查询以及考试历史成绩的查询等等。


"""

three_items_str="""
日志管理
信息发布
教师授权
用户管理
专家答疑
试题管理
考场监控
考试发布
修改密码
登录系统

提交问题
成绩查询
在线考试
查看日志
修改密码
登录系统

"""

# def d():
    

class Line:
    def __init__(self):
        # self.start = start
        # self.end = end
        # self.text = text
        self.id=""
        self.name=""
        self.source=""
        self.target=""
        self.target_node=""
        self.diagram_name="kaoshi"
        self.level=0
    # def __init__(self, start, end, text):
    #     self.start = start
    #     self.end = end
    #     self.text = text
    def make_target_str(self):
        self.target=self.target_node.id
        # print(self.target)

    def make_code(self):
        return f"""
            <mxCell id="line-{self.name}-{self.source}-{self.target}"
     style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
    edge="1" parent="1" source="{self.source}" target="{self.target}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>"""
        # return self.start + self.text + self.end

def make_code_line(diagram_name,level,name,source,target):
    return f"""
            <mxCell id="{diagram_name}-level-{level}-line-{name}"
     style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
    edge="1" parent="1" source="{source}" target="{target}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>"""


class Cell:
    def __init__(self) -> None:
        self.name=""
        self.id=""
        self.diagram_name="kaoshi"
        self.level=3
        self.id_num=3
        self.x=3
        # self.id=f"{self.diagram_name}-level-{self.level}-cell-{self.name}-{self.id_num}"

    # def __init__(self,diagram_name,level,name,id_num,x) -> None:
    #     # self.name=""
    #     # # self.id=""
    #     # self.diagram_name="kaoshi"
    #     # self.level=3
    #     # self.id_num=3
    #     self.x=x

    #     self.diagram_name=diagram_name
    #     self.level=level
    #     self.name=name
    #     self.id_num=id_num
    #     self.id=f"{self.diagram_name}-level-{self.level}-cell-{self.name}-{self.id_num}"

    def make_id(self):
        self.id=f"{self.diagram_name}-level-{self.level}-cell-{self.name}-{self.id_num}"

    def three_level_make(self):
        # id_num=4
        # id="{self.diagram_name}-level-{self.level}-cell-{self.name}-{self.id_num}"
        return f"""
        <mxCell id="{self.id}" value="{self.name}" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
        <mxGeometry x="{self.x}" y="540" width="120" height="60" as="geometry" />
        </mxCell>"""


def three_level_make(name,id_num,x):
    # id_num=4
    return f"""
      <mxCell id="V5LRMonKBBMW_ER4-Cw3-{id_num}" value="{name}" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
      <mxGeometry x="{x}" y="540" width="120" height="60" as="geometry" />
    </mxCell>"""


import  listUtil
# listUtil.remove
# imp 
# ListU 
# li

def  main():
    id_num=4
    x=110
    three_items=three_items_str.split("\n")
    three_items=listUtil.remove_all(lst=three_items,what="")

    for i in  three_items:
        # print(f"*** {i}")
        # three_level_node=three_level_make(name=i,id_num=id_num,x=x)
        cell=Cell()
        cell.x=x
        cell.id_num=id_num
        cell.name=i
        cell.make_id()
        
        # cell.id_num=id_num
        three_level_node=cell.three_level_make()

        id_num+=1
        x+=200
        
        

        print(three_level_node)


def colStrToSelfInit(colsStr):
    # colsStr="diagram_name,level,name,id_num"
    cols=colsStr.split(",")
    # str=str.replace("\n","")

    # print(str)

    for col in cols:
        print(f"self.{col}={col}")

学生子系统_cell=Cell()
学生子系统_cell.level=2
学生子系统_cell.name="学生子系统"
学生子系统_cell.make_id()
line=Line()
line.source=学生子系统_cell.id

def tars_str_to_lines(tars_str,src_id):
    # tars_str="""
    # *** 提交问题
    # *** 成绩查询
    # *** 在线考试
    # *** 查看日志
    # *** 修改密码
    # *** 登录系统"""
    out_code=""
    codeList=[]

    tars=tars_str.split("\n")
    tars=listUtil.remove_none(tars)
    x_start=110
    x_step=200
    target_node_x=x_start
    for tar in tars:
        # *** 
        tar=tar.replace("*** ","")
        line=Line()
        line.source=src_id
        target_node=Cell()
        target_node.x=target_node_x
        target_node.name=tar
        target_node.make_id()
        target_node_code=target_node.three_level_make()
        print(target_node_code)
        out_code+=target_node_code+"\n"
        line.target_node=target_node
        # make_id
        # def make_target_str(self):
        line.make_target_str()
        line_code=line.make_code()
        # line.target_node.
        print(line_code)
        out_code+=line_code+"\n"
        # make_code_line(diagram_name="kaoshi",level=3,name=tar,source=src_id,target=line.target_node.id)
        target_node_x+=x_step
        # line.target=f"{self.diagram_name}-level-{self.level}-line-{self.name}"
        # line.target=f"{学生子系统_cell.diagram_name}-level-{学生子系统_cell.level}-cell-{tar}-{学生子系统_cell.id_num}"
        # line.name=tar
        # line.make_code()
        # print(line.make_code())
    with open(f"out_{学生子系统_cell.diagram_name}.xml","w",encoding="utf-8") as f:
        f.write(out_code)


wbs_code="""
* 考试系统
** 学生子系统
*** 提交问题
*** 成绩查询
*** 在线考试
*** 查看日志
*** 修改密码
*** 登录系统

** 教师子系统
*** 日志管理
*** 信息发布
*** 教师授权
*** 用户管理
*** 专家答疑
*** 试题管理
*** 考场监控
*** 考试发布
*** 修改密码
*** 登录系统"""
# main()
tars_str="""
*** 提交问题
*** 成绩查询
*** 在线考试
*** 查看日志
*** 修改密码
*** 登录系统"""
tars_str_to_lines(tars_str,src_id=学生子系统_cell.id)
# D:\proj\python\my_util_py_pub\selfCode.py
self_code_path=r"D:/proj/python/my_util_py_pub/selfCode.py"

# def self_code_to_def(lines):
#     # lines=f.readlines()
#     for line in lines:
#         # line=line.replace("\n","")
#         line=line.replace("self.","")
#         # line=line.replace("=","")
#         # line=line.replace(" ","")
#         print(f"def {line}():")
#         print(f"    self.{line}={line}")


def self_code_to_def(code):
    # lines=f.readlines()
    code=code.replace("self.","")
    return code
    # for line in lines:
    #     # line=line.replace("\n","")
    #     line=line.replace("self.","")
    #     # line=line.replace("=","")
    #     # line=line.replace(" ","")
    #     print(f"def {line}():")
    #     print(f"    self.{line}={line}")

def main_self_code_to_def():

    with open(self_code_path,"r") as f:
        # lines=f.readlines()
        code=f.read()
        code=self_code_to_def(code)
        print(code)
        # self_code_to_def(lines)
        # for line in lines:
        #     line=line.replace("\n","")
        #     line=line.replace("self.","")
        #     line=line.replace("=","")
        #     line=line.replace(" ","")
        #     print(f"def {line}():")
        #     print(f"    self.{line}={line}")


def dfs(n):
    if n>5:
        return
    # print(1)
    print(n)
    # 这个函数里面也在调用这个函数 就是递归
    dfs(n+1)


# dfs(1)