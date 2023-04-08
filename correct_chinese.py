# pip install -U pycorrector

# D:\proj\python\my_util_py_pub>python --version
# Python 3.7.4
# ModuleNotFoundError: No module named 'pycorrector'
import threading
print('start pycorrector  load') 
import pycorrector
print('end pycorrector  load') 
# tim 
import time


# start_time = time.time()


# python 计时

def py_corrector_do(string):
    print('start py_corrector_do')
    start_time = time.time()
    # '少先队员因该为老人让坐'

    corrected_sent, detail = pycorrector.correct(string)
    end_time=time.time() 
    # end_time=time.time() - start_time
    print(corrected_sent, detail)
    print('use  sec ',end_time-start_time)
    # use  sec  5.703925609588623

# python 开一个线程 去运行 耗时的
# string='少先队员因该为老人让坐'
string="""运行时 is_persent(x)总是提示出现：
TypeError: is_persent() takes 1 positional argument but 2 were given

2、解决方法
解决方法很明显了，就是在类函数中加上self，问题就解决了
主要原因是，在类调用类内部函数时，会自动传入self参数；举个例子如果函数中不写self，那么参数只有x，但是在函数调用是传入参数是（self，x）两个参数，所以函数就会报错。
————————————————
版权声明：本文为CSDN博主「suhao0911」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/suhao0911/article/details/91045818"""

#  [('类', '雷', 139, 140), ('权协', '宣泄', 284, 286)]
# vue 下标  高亮 

# 解决python threading报错：Exception in thread Thread-5: takes 1 positional argument but 11 were given_自由学者亻伊宸的博客-CSDN博客_import threading 报错
# https://blog.csdn.net/weixin_45386875/article/details/114649086
# 创建线程t1,并添加到线程数组
# args=(string,) 逗号也是必须的 
t1 = threading.Thread(target=py_corrector_do, args=(string,)) # 已经创建好的一个线程
# threads.append(t1) # 追加到线程数组
# TypeError: py_corrector_do() takes 1 positional argument but 11 were given

print("out  thread")

t1.start()

print("t1  thread start yes")
t1.join()
print("t1  thread  join")

# python多线程用法及与单线程耗时比较_Python热爱者的博客-CSDN博客
# https://blog.csdn.net/qdPython/article/details/108798970
 

# 少先队员应该为老人让座 [('因该', '应该', 4, 6), ('坐', '座', 10, 11)]
# use  14.391676425933838

# shibing624/pycorrector: pycorrector is a toolkit for text error correction. 文本纠错，Kenlm，ConvSeq2Seq，BERT，MacBERT，ELECTRA，ERNIE，Transformer，T5等模型实现，开箱即用。
# https://github.com/shibing624/pycorrector

# # conda active py374
# CommandNotFoundError: No command 'conda active'.
# Did you mean 'conda activate'?
# conda activate  py374


# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "d:\proj\python\my_util_py_pub\correct_chinese.py", line 8, in <module>
#     corrected_sent, detail = pycorrector.correct('少先队员因该为老人让坐')
#   File "D:\software\anaconda\envs\py374\lib\site-packages\pycorrector\corrector.py", line 288, in correct
#     maybe_errors, proper_details = self.detect_sentence(sentence, idx, **kwargs)
#   File "D:\software\anaconda\envs\py374\lib\site-packages\pycorrector\detector.py", line 372, in detect_sentence
#     self.check_detector_initialized()
#   File "D:\software\anaconda\envs\py374\lib\site-packages\pycorrector\detector.py", line 114, in check_detector_initialized  
#     self._initialize_detector()
#   File "D:\software\anaconda\envs\py374\lib\site-packages\pycorrector\detector.py", line 74, in _initialize_detector
#     raise ImportError('pycorrector dependencies are not fully installed, '
# ImportError: pycorrector dependencies are not fully installed, they are required for statistical language model.Please use "pip install kenlm" to install it.if you are Win, Please install kenlm in cgwin.


# (py374) D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\correct_chinese.py"
# Downloading data from https://deepspeech.bj.bcebos.com/zh_lm/zh_giga.no_cna_cmn.prune01244.klm
# 2953396224/2953395058 [==============================] - 1107s 0us/step
# 2022-12-03 22:34:48.960 | DEBUG    | pycorrector.detector:_initialize_detector:89 - Loaded language model: C:\Users\25004/.pycorrector/datasets/zh_giga.no_cna_cmn.prune01244.klm
# 少先队员应该为老人让座 [('因该', '应该', 4, 6), ('坐', '座', 10, 11)]
