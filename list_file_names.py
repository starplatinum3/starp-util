
# dir_name=rf"D:\proj\bishe\handy_zucc\src\main\java\cn\zucc\edu\handyzucc\entity"
# dir_name=rf"D:"
# dir_name=rf"D:\\"
# dir_name=rf"D:/"
# dir_name=rf"D:/"
# D:\download
# D:\download
# E:\file
# dir_name=rf"D:\download"

dir_name=rf"E:\file"
# dir_name=rf"dpc"


# Alpaca-Lora (羊驼-Lora)_ 轻量级 ChatGPT 的开源实现（对标 Standford Alpaca）.mhtml
# Alpaca
# keyword='Alpaca'
# keyword='doc'
# keyword='docx'
# keyword='简历'
# keyword='starp'
# keyword='毕设'
keyword='eo'
# "Pyt"
import os 
for filename  in  os.listdir(dir_name):
    # print(filename)
    # if filename.startswith("pip")
    # if "pip" in filename:
    if keyword in filename:
        abs_path=os.path.join(dir_name,filename)
        print(abs_path)
    # filename_enitty_name=filename.split(".java")[0]
    # print(filename_enitty_name)
"""
pip_down.cmd
pip_down.py
pip_links.js
pip_links_this_platform.html
"""
# D:\download
# Admin
# Article
# Bill
# BillExtend
# Class
# Dorm
# Event
# EventReg
# EventRegExtend
# Follow
# Maintenance
# MaintenanceExtend
# Notice
# Post
# PostCmt
# PostFavorite
# PostVote
# Shop
# ShopCmt
# Teacher
# Test
# User

# 管理
# 文章
# 账单
# 账单扩展
# 班
# 宿舍
# 事件
# 事件注册
# 事件规则扩展
# 跟随
# 维修
# 维护扩展
# 注意
# 邮递
# 发布命令
# 发布收藏夹
# 投票后
# 商店
# 车间Cmt
# 教师
# 测验
# 使用者