# Python使用try...except...输出详细错误信息（比如报错具体位置在第几行）
 
import sys
import traceback
 
try:
    print(1/1)
    print(1/0)
    print(1/1)
except Exception as e:
    print(1/1)
    # 这个是输出错误的具体原因
    print(e) # 输出：division by zero
    print(sys.exc_info()) # 输出：(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001A1A7B03380>)
    
    # 以下两步都是输出错误的具体位置，报错行号位置在第几行
    print('\n','>>>' * 20)
    print(traceback.print_exc())
    print('\n','>>>' * 20)
    print("traceback.format_exc()")
    print(traceback.format_exc())
    '''
    两句输出结果大体相同： 记得下面有转义符 如果不用 \\ 那么 三个点的多行注释会报错
    Traceback (most recent call last):
        File "d:\\Backup\\Downloads\\Untitled-1.py", line 8, in <module>
            print(1/0)
          ~^~
    ZeroDivisionError: division by zero
    None
    '''
 
    '''
    ------------------------------------------------------------------------------------
    以下为拓展资料
    模块 sys 中，有两个方法可以返回异常的全部信息，分别是 exc_info() 和 last_traceback()，这两个函数有相同的功能和用法，此处仅以 exc_info() 方法为例。
    sys.exc_info() 方法会将当前的异常信息以元组的形式返回，该元组中包含 3 个元素，分别为 type、value 和 traceback，它们的含义分别是：
        @ type：异常类型的名称，它是 BaseException 的子类（有关 Python 异常类，可阅读《Python常见异常类型》一节）
        @ value：捕获到的异常实例。
        @ traceback：是一个 traceback 对象。
    ------------------------------------------------------------------------------------
    traceback.print_exc()：将异常传播轨迹信息输出到控制台或指定文件中。
    traceback.format_exc()：将异常传播轨迹信息转换成字符串。
    一般我们常用 print_exc()
    实际上我们常用的 print_exc() 是 print_exc([limit[, file]]) 省略了 limit、file 两个参数的形式。
    而 print_exc([limit[, file]]) 的完整形式是 print_exception(etype, value, tb[,limit[, file]])，
    在完整形式中，前面三个参数用于分别指定异常的如下信息：
        @ etype：指定异常类型；
        @ value：指定异常值；
        @ tb：指定异常的traceback 信息；
    '''