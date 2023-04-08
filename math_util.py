


# python 统计每一段的 最大值，比如 100-200内的最大 和 200-300内的最大
# 比如列表有这些数字 [145,146,147,178,243,253,254,255,345,356,367]
# 结果是  
# {
#     "100-200":178,
#      "200-300":255,
#       "300-400":367,
# }
# [145,146,147,178, )  243,253,254,255, )  345,356,367)  ]

def get_range(max_num=111,step=100,):
    # step=100
    # for i in 
    # max_num=111
    ranges = {}
    for i in range(0,max_num,step):
        # print(i)
        # print(i+step)
        # print(range(i,i+step))
        key="{}-{}".format(i,i+step)
        ranges[key]=range(i,i+step)
    # ranges = {"100-200": range(100, 201), "200-300": range(200, 301), "300-400": range(300, 401)}
    return ranges

def get_max_values(nums = [145,146,147,178,243,253,254,255,345,356,367]):
    """
    https://ask.csdn.net/questions/7905062?weChatOA=weChatOA1
    python 统计每一段的 最大值，比如 100-200内的最大 和 200-300内的最大
    比如列表有这些数字 [145,146,147,178,243,253,254,255,345,356,367]
    结果是  
    {
        "100-200":178,
        "200-300":255,
        "300-400":367,
    }
    [145,146,147,178, )  243,253,254,255, )  345,356,367)  ]
    {'0-5000': 3250, '5000-10000': 7013, '15000-20000': 15299, '20000-25000': 21236, '30000-35000': 30316}
    
    """
    # nums = [145,146,147,178,243,253,254,255,345,356,367]
    # ranges = {"100-200": range(100, 201), "200-300": range(200, 301), "300-400": range(300, 401)}
    ranges=get_range(max_num=40000,step=5000)
    max_values = {}
    
    for key in ranges:
        values_in_range = []
        for num in nums:
            if num in ranges[key]:
                values_in_range.append(num)
        if len(values_in_range)==0:
            continue
        max_values[key] = max(values_in_range)
        # ValueError: max() arg is an empty sequence
    
    # print(max_values)
    return max_values
