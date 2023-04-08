# 放在第一行的话 会用这个python  !/usr/bin/env python# -*-coding:utf-8 -*-
#!/usr/bin/env python# -*-coding:utf-8 -*-
# annotation.py
 
''' 文档快速生成注释的方法介绍,首先我们要用到__all__属性在Py中使用为导出__all__
中的所有类、函数、变量成员等在模块使用__all__属性可避免相互引用时命名冲突'''
 
__all__ = ['Login', 'Shop']
 
 
class Login(object):
    ''' 测试注释一可以写上此类的作用说明等 例如此方法用来写登录 '''
 
    def __init__(self):
        ''' 初始化你要的参数说明 '''
        pass
 
    def check(self):
        ''' 协商你要实现的功能说明 '''
        pass
 
 
class Shop(object):
    ''' 商品类所包含的属性及方法 update改/更新 find查找 delete删除 create添加 '''
 
    def __init__(self):
        ''' 初始化商品的价格、日期、分类等 '''
        pass
 
    def upDateIt(self):
        ''' 用来更新商品信息 '''
        pass
 
    def findIt(self):
        ''' 查找商品信息 '''
        pass
 
    def deleteIt(self):
        ''' 删除过期下架商品信息 '''
        pass
 
    def createIt(self):
        ''' 创建新商品及上架信息 '''
        pass
 
 
if __name__ == "__main__":
    import annotation
 
    print(help(annotation))