dict={"key":["value1","value2"]}

print(dict)

a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one':4.5, 'four': 9.3})
# a.update({'listKey':[4.5,'list'] })
a.update({['listKey']:[4.5,'list'] })
print(a)
version='version'
# {version:packs}

# {'key': ['value1', 'value2']}
# Traceback (most recent call last):
#   File "d:\proj\python\my_util_py_pub\map_test.py", line 8, in <module>
#     a.update({['listKey']:[4.5,'list'] })
# TypeError: unhashable type: 'list'
