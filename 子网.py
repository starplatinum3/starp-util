
# 某公司申请到一个C类网络，由于有地理位置上的考虑必须切割成5__牛客网
# https://www.nowcoder.com/questionTerminal/536665c047c948b8bec3339f84a33c3f?source=relative

"""
链接：https://www.nowcoder.com/questionTerminal/536665c047c948b8bec3339f84a33c3f?source=relative
来源：牛客网

某公司申请到一个C类网络，由于有地理位置上的考虑必须切割成5个子网，请问子网掩码要设为（）
255.255.255.224
255.255.255.192
255.255.255.254
255.285.255.240"""

subnet_cnt=5
# python 代码 转化为 java

def get_should_bit_cnt(subnet_cnt):


    for bit_cnt in range(100):
        pow_of_bit_cnt=pow(2,bit_cnt)
        # print(pow_of_bit_cnt)
        if pow_of_bit_cnt>subnet_cnt:
            return bit_cnt,pow_of_bit_cnt
    return None

should_bit_cnt,pow_of_bit_cnt=get_should_bit_cnt(subnet_cnt)

print(should_bit_cnt)

def mask(should_bit_cnt):
    mask_str=""
    for i in range(8):
        if i<should_bit_cnt:
            mask_str+="1"
        else:
            mask_str+="0"
    return mask_str

# python  二进制转十进制

# int('1010',base=2)。
mask_of_subnet=mask(should_bit_cnt)

# 链接：https://www.nowcoder.com/questionTerminal/536665c047c948b8bec3339f84a33c3f?source=relative
# 来源：牛客网
print(f"""
由于是C类网络，所以前面是255.255.255不用解释。由于题目要求{subnet_cnt}个子网，2^{should_bit_cnt}={pow_of_bit_cnt}>{subnet_cnt},
所以至少需要{should_bit_cnt}位二进制才能存放下{subnet_cnt}个子网。所以最后一个子网掩码为{mask_of_subnet}，
结果等于224,综上，结果为255.255.255.224。
""")
# mask(should_bit_cnt)
print(mask_of_subnet)
# subnet
# SubnetAnalysis