# 三、.*和.+正则提取的区别
# .：匹配任意字符
# *：匹配0个或多个字符
# ?：非贪婪模式，在符合的条件下，尽可能少的匹配(尽可能短的匹配)
import re

# itemName='questionInfo'
itemName='item'

htmlPath=r"D:\proj\bishe\QuestionWechatApp\pages\answer\index.wxml"

"""

 let  item  = {
 "isChose": "",
"item": "",
"id": "",
"judge==1?'succ':item.judge==0?'err':''": "",
"judge==1": "",
"judge==0": "",

}

"""


with open(htmlPath, "r", encoding="utf-8") as f:
    html_data=f.read()


str2 = "aabab"
str3 = """
 </view>
    <image wx:if="{{questionInfo.picUrl}}" style="width: 100%; height: 200px; background-color: #fff;" mode="aspectFit" src="{{questionInfo.picUrl}}" data-src="{{questionInfo.picUrl}}" catchtap="showPic"></image>
    <audio wx:if="{{questionInfo.audio}}" style="width:{{windowWidth}}px;margin-bottom:10px;text-align:center;" src="{{questionInfo.audio}}" id="myAudio" controls loop></audio>
    
    <view wx:if="{{questionInfo.video}}" class='view' style='width:{{windowWidthpx}};height:225px;' bindtap='showVideo' hidden='{{showVideo}}'></view>
    <video wx:if="{{questionInfo.video}}" hidden='{{!showVideo}}' src="{{questionInfo.video}}" objectFit="cover" style="width:{{windowWidth}}px;margin-bottom:10px;" page-gesture="true" show-fullscreen-btn="false" id="myVideo" bindpause='hideVideo' bindended='hideVideo' controls>
    </video>
    <!--答案选择 - 单选-->"""
a = re.findall('a.*?b',str2)	#结果：['aab', 'ab']
# b = re.findall('a.+?b',str2)	#结果：['aab']
# b = re.findall('{{questionInfo\..*?}}',str3)
# itemName='questionInfo'
# itemName='item'

pattern='{{#itemName#\.(.*?)}}'.replace('#itemName#',itemName)
# b = re.findall('{{questionInfo\.(.*?)}}',str3)
# findAllThey = re.findall(pattern,str3)
findAllThey = re.findall(pattern,html_data)
import listUtil
findAllThey=listUtil.remove_same(findAllThey)
# {
#     "a": "aab",
#     "b": "ab"
# }
fieldNameLines=""
for fieldName in findAllThey:
    # fieldNameLine=f'"{fieldName}": "",'
    fieldNameLine=f'"{fieldName}": "1",'
    fieldNameLines+=fieldNameLine+'\n'
print(fieldNameLines)
# itemJs=f''' {itemName }  = {
#  {fieldNameLines}
# }'''


# listUtil.re 
# python 去重 list

# python 生成 随机 名字 

itemJs=''' let  {itemName}  = {
 {fieldNameLines}
}'''
itemJs=itemJs.replace('{itemName}',itemName)
itemJs=itemJs.replace('{fieldNameLines}',fieldNameLines)
print(itemJs)
# re group 
# questionInfoFind=re.search('{{questionInfo\.(.*)?}}', str3)
questionInfoFind=re.search('{{questionInfo\.(.*?)}}', str3)
questionInfoFindGroup= questionInfoFind.group()
questionInfoFindGroup1=  questionInfoFind.group(1)
print("questionInfoFindGroup1")
print(questionInfoFindGroup1)
print("questionInfoFindGroup")
print(questionInfoFindGroup)
# print(" questionInfoFind.group(2)")
# print( questionInfoFind.group(2))
# print(re.search('{{questionInfo\.(.*)?}}', str3).group())

#  <image wx:if="{{questionInfo.picUrl}}"
print(a)
# print(b)
# .?：匹配aab和ab ，因为可以匹配0个字符，所以可以匹配得到ab
# .+?：匹配aab，因为+必须a和b中间至少有一个字符，所以排除了ab

# 四、起始有无^的区别
str2 = "aabab"
c = re.findall('.*',str2)	#结果：['aabab', '']
d = re.findall('^.*',str2)	#结果：['aabab']
print(c )
print(d)

# ['aab', 'ab']
# ['aab']
# ['aabab', '']
# ['aabab']
# ————————————————
# 版权声明：本文为CSDN博主「weixin_43890704」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43890704/article/details/126100731