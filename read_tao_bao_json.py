
import pandas as pd

dir_name=r"D:\download"
out_dir_name=r"D:\file"

# keyword="手机"
# name="当天发送好礼!小米红米Note10Pro 8+256GB 5G手机 天玑1100旗舰 67W闪充 小米官方旗舰官网正品店Redmi"


# keyword="面包"
keyword="香蕉"
# keyword="香蕉"

# name="小鸡收腹全麦欧包面包带馅五谷杂粮低0无糖精脂肪卡非无油软代餐"
# name=keyword
# 云南自家栽种威尼斯绿皮香蕉无药水新鲜水果自然成熟现砍现发包邮
# name='云南自家栽种威尼斯绿皮香蕉无药水新鲜水果自然成熟现砍现发包邮'
name='云南高山香蕉10斤新鲜当季水果芭蕉苹果蕉小米蕉青香蕉自然熟整箱'

import  os 



def parse_file_name(file_name):
    parts=file_name.split("_")
    time_str=file_name.replace(".json","")
    time_str=time_str.replace(f'{parts[0]}_{parts[1]}_',"")
    return {
        "type":parts[0],
        "keyword":parts[1],
        "time_str":time_str
        # "page":parts[-1]
    }

df_merged=pd.DataFrame()

file_name_set=set()
all_abs_path=[]
all_file_name=[]
def get_type_name(file_name):
    return file_name.split("_")[1]

for file_name in os.listdir(dir_name):
    if not file_name.startswith("taobao"):
        continue
    if file_name.endswith(".json"):
        file_path=os.path.join(dir_name,file_name)
        
        type_name=get_type_name(file_name)
        file_name_set.add(type_name)
        all_abs_path.append(file_path)
        all_file_name.append(file_name)
        try:
            df=pd.read_json(file_path)
        except Exception as e:
            print(e)
            print("file_path")
            print(file_path)
        
        # print("df.columns")
        # print(df.columns)
        parsed_file_name=parse_file_name(file_name)
        have_keyword =keyword in parsed_file_name['keyword']
        # if parsed_file_name['keyword']==keyword:
        if have_keyword:
            time=parsed_file_name["time_str"]
            # time=pd.to_datetime(parsed_file_name["time_str"])
            df["time"]=time
            # df.
            df_merged=df_merged.append(df) 
        # df.merge()
    #     df.to_csv(file_path.replace(".json",".csv"),index=False)
    # abs_file_name=os.path.join(dir_name,file_name)
    # pd.read_json(abs_file_name)

print(file_name_set)
# out_file_path=os.path.join(out_dir_name,f"{keyword}_all.csv")
# print("out_file_path")
# print(out_file_path)
# encoding="utf_8_sig"
"""
{'即热食品', '运动鞋', '火鸡', '柠檬', '柿子', '蛋糕', '手撕面包', '香蕉', '洗面奶', '糖豆', '电热水壶', '男装', '泡面', '充电宝', '保温杯', '蜜饯', '矿泉水', '热水器', '猪肉干', '小熊软糖', '葡萄', '手机', '番茄', '鱼片干', '辣条', '即时', '面包', '洗衣机', '床垫', '肉干', '烤鸭', '西瓜', ' 杏仁', '内裤', '鱿鱼丝', '瓜子', '马桶坐垫', '士力架', '速冻饺子', '电视', '连衣裙', '芬达', '内脏', '橘子', '凤爪', 'java', '栗子', '牙刷', '剝壳嗑瓜子', '麻花', '脉动', '剃须刀', '芒果', '止疼药', '水蜜桃', '洋葱', '洗发水', '男士t恤', '马桶', '烤鸡', '海苔', '牛油果酱', '樱桃', '鸭翅膀', '发烧药', '紫菜', '电热毯', '热狗', '龙眼', '不锈钢脸盆', '空调', '洗衣液', '牙膏', '可乐', '柚子', '防晒霜', '肉包', '手套', '爆米花', '腰果', '雪碧', 'python', '荔枝', '薯片', '零食', '华为手机', '番石榴', '玉米片', '坚果', '被子', '棒棒糖', '饼干', '热干面', '手表', '止泻药', '石榴', '棉拖鞋', '杏仁', '联想', '椰子', '奶黄包', '帽子', '抽水马桶', '防窥膜', '电脑', '寿司', '巧克力', '洗脚盆', '香肠', '开心果', 'iphone', '女套装', '橄榄', '甘蔗', '李子', '鸭舌头', '电饭煲', '酒精', '话梅', '项链', '感冒药', '核桃', '床', '山楂', '床单', '优衣库'}
"""
# data_itemid
df_merged_groupby_data_itemid=df_merged.groupby(by='data_itemid')


# df_merged.to_csv(out_file_path,index=False,encoding="utf_8_sig")



# df_merged.to_csv(out_file_path,index=False,encoding="utf-8")
# df_merged.to_csv(out_file_path,index=False,encoding="gbk")
# to_csv encoding="utf-8" 乱码


# print("all_abs_path")
# print(all_abs_path)
# print("all_file_name")
# print(all_file_name)


# def ged(file_name):
#     file_name.replace(".json","")
#     file_name.replace(``,"")


# file_name=r"D:\download\taobao_手机_2022_12_22_8_58_15.json"
# parsed_file_name=parse_file_name(file_name)
# print("parsed_file_name")
# print(parsed_file_name)

print("df_merged")
print(df_merged)

# # parsed_file_name
# # {'type': 'D:\\download\\taobao', 'keyword': '手机', 'time_str': '2022_12_22_8_58_15'}
# df=pd.read_json(r"D:\download\taobao_手机_2022_12_22_8_58_15.json")
# print(df)
# do_draw=False
do_draw=True
if do_draw:
    import matplotlib.pyplot as plt

    # 支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # name="[下单优惠910]OPPO K10 oppok10手机新款oppo手机官方旗舰店官网k9s k10pro新品0ppo限量版5g0ppok7x por"
    # name="MIUI/小米 Redmi 8A红米8a手机7a大电池老人学生智能note7手机"

    # name="MIUI/小米 Redmi Note 12 Pro 5g 手机官方旗舰红米note12pro正品"
    # df_merged.plot(x='itemName',y='afterCoupon')

    # df_merged[df_merged['itemName']==name].plot(x='itemName',y='afterCoupon')
    # plt 中文
    # df_merged[df_merged['itemName']==name].plot(x='time',y='afterCoupon',title=name)
    df_merged[df_merged['itemName'].str.contains( name)].plot(x='time',y='afterCoupon',title=name)
    plt.show()
    # plot 画出 点的 数字 

    # D:\proj\python\my_util_py_pub\read_tao_bao_json.py