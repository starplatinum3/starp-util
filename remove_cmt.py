code="""
package com.mindskip.xzs.event;

import com.mindskip.xzs.domain.ExamPaperAnswerInfo;
import org.springframework.context.ApplicationEvent;

/**
 * @version 3.3.0
 * @description: The type Calculate exam paper answer complete event.
 * Copyright (C), 2020-2021, 武汉思维跳跃科技有限公司
 * @date 2021/5/25 10:45
 */
public class CalculateExamPaperAnswerCompleteEvent extends ApplicationEvent {


    private final ExamPaperAnswerInfo examPaperAnswerInfo;


    /**
     * Instantiates a new Calculate exam paper answer complete event.
     *
     * @param examPaperAnswerInfo the exam paper answer info
     */
    public CalculateExamPaperAnswerCompleteEvent(final ExamPaperAnswerInfo examPaperAnswerInfo) {
        super(examPaperAnswerInfo);
        this.examPaperAnswerInfo = examPaperAnswerInfo;
    }

    /**
     * Gets exam paper answer info.
     *
     * @return the exam paper answer info
     */
    public ExamPaperAnswerInfo getExamPaperAnswerInfo() {
        return examPaperAnswerInfo;
    }

}
"""

import os
# os.listdir()

# python 传入 函数
def getallfilesofwalk_do(dir,callback):
    """使用listdir循环遍历"""
    if not os.path.isdir(dir):
        # 文件 
        # print dir
        callback(dir)
        return
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            # pass
            abs_path=os.path.join(root, file)
            callback(abs_path)
        # print os.path.join(root, file)


def remove_cmt_file(abs_path):
    with open(abs_path,"r",encoding="utf-8") as f:
        data=f.read()
    code=data
    idx=code.find("武汉思维跳跃科技")
    # idx=code.index("武汉思维跳跃科技")
    if idx==-1:
        return 
    out_data=remove_cmt(data)
    # lines=data.split("\n")
    # cmt_data=""
    # # cmt_line_mark=default
    # # 'product="default"'
    # cmt_line_mark='product="nosdcard"'
    # # 'product="default"'
    # for line in lines:
    #     if cmt_line_mark in line :
    #         # line=
    #         cmt_data+="<!-- "+line+" -->"
    #         # cmt_line()
    #     else:
    #         cmt_data+=line
    #     cmt_data+="\n"
    # print(cmt_data)
    with open(abs_path,"w+",encoding="utf-8") as f:
        f.write(out_data)


def remove_cmt(code:str):
    idx=code.find("武汉思维跳跃科技")
    # idx=code.index("武汉思维跳跃科技")
    if idx==-1:
        return code
    
    lines=code.split("\n")

    now_cmt_removing=False
    remove_once=False
    remove_end=False
    out_lines=[]
    for  line in lines:
        if remove_once and not now_cmt_removing:
            print(line)
            out_lines.append(line)
            continue
        line_striped=line.strip()
        if  line_striped.startswith("/**"):
            now_cmt_removing=True
            remove_once=True
        elif line_striped.startswith("*/"):
            # print(line)
            now_cmt_removing=False
            remove_end=True
        if now_cmt_removing:
            # */ 要删掉 
            # if remove_end:
            #     remove_end=False
            # else:
            #     print(line)
            continue
        else:
            if remove_end:
                remove_end=False
            else:
                # print(line)
                out_lines.append(line)
            # print(line)
    out_data="\n".join(out_lines)
    return out_data


# getallfilesofwalk_do(r"D:\proj\Android\recorder_res\res_def\res",remove_cmt_file)

# getallfilesofwalk_do(r"D:\proj\springBoot\exam-sys-db\src\main\java\com\mindskip\xzs\event",remove_cmt_file)
# getallfilesofwalk_do(r"D:\proj\springBoot\exam-sys-db\src\main\java",remove_cmt_file)

getallfilesofwalk_do(r"D:\proj\springBoot\exam-sys-db2\src\main\java",remove_cmt_file)