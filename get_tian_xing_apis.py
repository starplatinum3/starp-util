
apis=[
    {
        "href": "https://www.tianapi.com/apiview/175",
        "textContent": "收货地址解析"
    },
    {
        "href": "https://www.tianapi.com/gethttp/175",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/182",
        "textContent": "判断题"
    },
    {
        "href": "https://www.tianapi.com/gethttp/182",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/196",
        "textContent": "微信热搜榜"
    },
    {
        "href": "https://www.tianapi.com/gethttp/196",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/239",
        "textContent": "地区搜索"
    },
    {
        "href": "https://www.tianapi.com/gethttp/239",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/174",
        "textContent": "每日英语"
    },
    {
        "href": "https://www.tianapi.com/gethttp/174",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/181",
        "textContent": "彩虹屁"
    },
    {
        "href": "https://www.tianapi.com/gethttp/181",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/185",
        "textContent": "百科题库"
    },
    {
        "href": "https://www.tianapi.com/gethttp/185",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/188",
        "textContent": "垃圾分类新闻"
    },
    {
        "href": "https://www.tianapi.com/gethttp/188",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/97",
        "textContent": "垃圾分类"
    },
    {
        "href": "https://www.tianapi.com/gethttp/97",
        "textContent": "立即调试"
    },
    {
        "href": "https://www.tianapi.com/apiview/223",
        "textContent": "全网热搜榜"
    },
    {
        "href": "https://www.tianapi.com/gethttp/223",
        "textContent": "立即调试"
    }
]

import requests

def get_api(url):
    # "https://www.tianapi.com/gethttp/223"
    r = requests.get(url)
    # return r.json()
    return r.json()["newslist"][0]["content"]

url="https://www.tianapi.com/gethttp/223"
r = requests.get(url)
print(r.text)

def main():
    for i in apis:
        print(i)
        
        href=i["href"]
        print(href)
        # 使用request进行post请求
        response = requests.request('get',href,{})
        print(response.text)
