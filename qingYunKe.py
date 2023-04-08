import urllib
import requests
def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
while True:
       msg = input().rstrip()
       print("原话>>", msg)
       res = qingyunke(msg)
       print("青云客>>", res)

# 计算机专业可以做什么职业，需要学习什么课程
# 原话>> 计算机专业可以做什么职业，需要学习什么课程
# 青云客>> 菲菲会的可多了，了解菲菲的全部本领，请发送：help

# 青云客>> 菲菲内置多种功能，通过发送命令可执行特殊操作{br}★★ 示例 ★★{br}　查询天气预报信息，示例：天气 深圳{br}手机、ＩＰ地址归属，示例：归属 手机或IP{br}　　　邮政编码及地区查询：邮编 514000{br}　　计算简单的算术，示例：计算 15+13{br}　　　查询成语介绍，示例：成语 一心一意{br}按歌曲名称查询歌词，示例：歌词 歌曲名称{br}　　中译英、英译中，示例：翻译 i love you{br}　查询星座今日运势，示例：星座 天秤座{br}　查询星座介绍请直接发送：天秤座{br}汉字五笔拼音笔画查询示例：礡字{br}　　想看笑话，请直接发送：笑话
"""
原话>> 计算机
青云客>> 竭诚为您服务

原话>> 土木
青云客>> 乞衣
"""