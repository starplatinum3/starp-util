# python 求掩码地址


# 子网掩码地址转长度
def netmask_to_bit_length(netmask):
    """
    >>> netmask_to_bit_length('255.255.255.0')
    24
    >>>
    """
    # 分割字符串格式的子网掩码为四段列表
    # 计算二进制字符串中 '1' 的个数
    # 转换各段子网掩码为二进制, 计算十进制
    return sum([bin(int(i)).count('1') for i in netmask.split('.')])

# 子网掩码长度转地址
def bit_length_to_netmask(mask_int):
    """
    >>> bit_length_to_netmask(24)
    '255.255.255.0'
    >>>
    """
    bin_array = ["1"] * mask_int + ["0"] * (32 - mask_int)
    tmpmask = [''.join(bin_array[i * 8:i * 8 + 8]) for i in range(4)]
    tmpmask = [str(int(netmask, 2)) for netmask in tmpmask]
    return '.'.join(tmpmask)

def and_ip(ip, mask):
    """
    网段
    >>> and_ip('
    """
    ip = ip.split('.')
    mask = mask.split('.')
    return '.'.join([str(int(i) & int(j)) for i, j in zip(ip, mask)])
# https://blog.csdn.net/qq_37746897/article/details/109847131
# python 
if __name__ == '__main__':
    # print (netmask_to_bit_length('255.255.255.0'))
    bit_len=netmask_to_bit_length('255.255.255.128')
    print ("bit_len")
    print (bit_len)
    print (bit_length_to_netmask(23))
    # bit_len
    # 25
    # 255.255.254.0
    bin_128=bin(128)
    print("bin_128",bin_128)
    # bin_128 0b10000000
    bin_255=bin(255)
    print("bin_255",bin_255)
    # bin_255 0b11111111

    # and_is=128^255
    and_is=128&255
    print("and_is",and_is)
    # and_is 127
    # and_is 128
    anded_ip=and_ip("128.96.39.9","255.255.255.128")
    print("anded_ip",anded_ip)
    # anded_ip 128.96.39.0
    # EF 

    # wangduan=and_ip('192.168.10.1','255.255.255.0')
    wangduan=and_ip('192.168.10.2','255.255.255.0')
    # wangduan=and_ip('192.168.10.3','255.255.255.0')
    print("wangduan")
    print(wangduan)
#     IP 地址:192.168.12.72 ，子网掩码为:255.255.255.192，写出该地址所在网段的网络地址和广播地址?_百度知道
# https://zhidao.baidu.com/question/214461634.html
#     wangduan
# 192.168.10.0
#     wangduan
# 192.168.10.0