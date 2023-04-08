from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions  as EC
from selenium.webdriver.common.by import By
import time

#不显示浏览器
'''opt =Options()
opt.add_argument('--headless")
opt.add_argument('--disable-gpu")                 

web=Chrome(options=opt)'''

web=Chrome()
web.get("https://www.icourse163.org/")
#print(web.pagesource) 页面源代码
def login():
    el=web.find_element_by_xpath('//*[@id="j-topnav"]/div/a')
    el.click()
    time.sleep(5)
    #关闭同意
    try:
        el=web.find_element_by_xpath('//*[@id="privacy-ok"]')
        el.click()
    except:
        pass
login()
#findRealPage()
time.sleep(3)
fw=open('d:\grade.txt','w')    
url=r'http://www.icourse163.org/collegeAdmin/termManage/1463501446.htm#/tp/cdata?t=5&eid=1219475931&page=%d&sid=undefined'
for i in range(1,13):    #页面循环  24
    realurl=url%i
    web.get(realurl)
    time.sleep(5)
    inputs=web.find_elements_by_xpath("//textarea[starts-with(@id,'auto-id')]")
    inputList=[]
    for a in inputs:
        inputList.append(a.get_attribute('value'))

    for j in range(5,22):  #学生循环 22
        stu=r'//*[@id="j-termPublish-main-box"]/div/div/div[2]/div/div[3]/div/table/tbody/tr[%d]/td[3]/a[2]'
        realstu=stu%j
        #打开学生的成绩表
        time.sleep(2)
        #estu=web.find_element_by_xpath(realstu)
        
        #等待左侧菜单到可点击状态
        estu=WebDriverWait(web,10).until(EC.element_to_be_clickable((By.XPATH,realstu)))
        estu.click()
        #到新窗口
        web.switch_to.window(web.window_handles[-1])
        time.sleep(5)
        #选择题循环
        modify=0
        
        
        for k in range(1,61):
            eti=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[1]/div[2]/div[3]/p'                      
            realeti=eti%k
            etitext=web.find_element_by_xpath(realeti).text            
            if etitext.find('以下正确')==0:  #找到第一道错题
                print(etitext)
                for m in range(1,5): #选项
                    eoptiontext=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/label/div[2]/p'
                    realepotiontext=eoptiontext%(k,m)
                    tioptiontext=web.find_element_by_xpath(realepotiontext).text
                    print(tioptiontext,end=' ')
                    eoptions=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/input'
                    realeoptions=eoptions%(k,m)
                    checked=web.find_element_by_xpath(realeoptions).is_selected()
                    print(checked)

                    if tioptiontext=='函数的定义不可以嵌套，但函数的调用可以嵌套' and checked==True:
                        modify=modify-1
                    if tioptiontext=='函数的定义和函数的调用均可嵌套' and checked==True:
                        modify=modify+1
            elif etitext.find('执行以下代码，output.txt文件中的内容是')==0:  #找到第一道错题
                print(etitext)
                for m in range(1,5): #选项
                    eoptiontext=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/label/div[2]/p'
                    realepotiontext=eoptiontext%(k,m)
                    tioptiontext=web.find_element_by_xpath(realepotiontext).text
                    print(tioptiontext,end=' ')
                    eoptions=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/input'
                    realeoptions=eoptions%(k,m)
                    checked=web.find_element_by_xpath(realeoptions).is_selected()
                    print(checked)

                    if tioptiontext=='8;5;2;2' and checked==True:
                        modify=modify-1
                    if tioptiontext=='8522' and checked==True:
                        modify=modify+1
            elif etitext.find('下面代码的输出结果是(         )。')==0:  #找到第一道错题
                print(etitext)
                for m in range(1,5): #选项
                    eoptiontext=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/label/div[2]/p'
                    realepotiontext=eoptiontext%(k,m)
                    tioptiontext=web.find_element_by_xpath(realepotiontext).text
                    print(tioptiontext,end=' ')
                    eoptions=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div/ul/li[%d]/input'
                    realeoptions=eoptions%(k,m)
                    checked=web.find_element_by_xpath(realeoptions).is_selected()
                    print(checked)

                    if tioptiontext=='mi' and checked==True:
                        modify=modify-1
                    if tioptiontext=='mir' and checked==True:
                        modify=modify+1      
        #填空题循环
                        
        #填空题学生答案
        tk=web.find_elements_by_xpath("//textarea[starts-with(@id, 'auto-id-')]")
        #for p in tk:
        #    print(p.get_attribute('value'))
            
        for n in range(71,76):
            tkf=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[2]/div[2]'            
            answer=r'//*[@id="courseLearn-inner-box"]/div/div[4]/div/div[1]/div[1]/div[%d]/div[3]/span[2]'
            rtkf=tkf%n
            tkftext=web.find_element_by_xpath(rtkf).text            
            if tkftext=='0.00/6.00':
                realg=eval(tkftext[:4]) #分数                
                rAnswer=answer%n
                AText=web.find_element_by_xpath(rAnswer).text
                stuAtext=tk[n-71].get_attribute('value')
                stulist=stuAtext.split()
                stdlist=AText.split()
                tkgrade=0
                if stulist[0]==stdlist[0] or stulist[0]==stdlist[1]:
                        tkgrade=3
                if len(stulist)>1 and stulist[1]==stdlist[1]:
                    tkgrade+=3
                modify=modify+(tkgrade-realg)
                print(stuAtext,AText)
                print('填空:',n,tkgrade-realg)
        print('应加:',modify)
        web.close()     
        web.switch_to.window(web.window_handles[0])

        #修改成绩
        print(inputList[j-2])
        ograde=inputList[j-2]
        newgrade=eval(ograde)+modify
        '''inputs[j-2].clear()
        inputs[j-2].send_keys(str(newgrade),Keys.ENTER)
        btn=web.find_element_by_class_name('u-btn u-btn-default j-xgbtn')
        btn.click()'''
        
        #写文件
        stuinfo='//*[@id="j-termPublish-main-box"]/div/div/div[2]/div/div[3]/div/table/tbody/tr[%d]/td[1]'
        realstu=stuinfo%j
        stutext= web.find_element_by_xpath(realstu).text
        begin=stutext.find('ZZU_')
        stutext=stutext[begin+4:]
        stuno=stutext[-12:]
        stuname=stutext[:-13]
        print(stuno,stuname,str(modify))
        print("*"*20)
        fw.write(stuno+'\t'+stuname+'\t'+ str(modify)+'\n')
        fw.flush()
        
fw.close()