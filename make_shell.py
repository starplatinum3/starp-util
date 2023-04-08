
# shift+enter 进入python 环境
def make_if_sh(val,op,val_right):
    if_stmt=f'if [ "${val}" {op} "{val_right}" ];then'
    return if_stmt

if_sh=make_if_sh('a','==','b')

print(if_sh)