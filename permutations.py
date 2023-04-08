

def  permutations_of_range(list1,start,end,result_list):
    if start==end:
        # print(list1)
        result_list.append(list1.copy())
        return
    else:
        for i in range(start,end+1):
            list1[start],list1[i]=list1[i],list1[start]
            #将第i个元素与首位元素交换
            permutations_of_range(list1,start+1,end,result_list)
            #子序列进行全排列
            list1[start], list1[i] = list1[i], list1[start]
            #将i个元素放回原位置，准备下一个元素的交换

def  permutations(list1,result_list):
    permutations_of_range(list1,0,len(list1)-1,result_list)
    # if start==end:
    #     print(list1)
    # else:
    #     for i in range(start,end+1):
    #         list1[start],list1[i]=list1[i],list1[start]
    #         #将第i个元素与首位元素交换
    #         permutations(list1,start+1,end)
    #         #子序列进行全排列
    #         list1[start], list1[i] = list1[i], list1[start]
    #         #将i个元素放回原位置，准备下一个元素的交换


# main 
if __name__ == '__main__':

    list1=['香蕉','苹果','梨子']

    res=[]
    # permutations(list1,0,len(list1)-1)
    permutations(list1,res)

    # print(list1)

    print(res)

    for i in res:
        str="-".join(i)
        print(str)

# ['香蕉', '苹果', '梨子']
# ['香蕉', '梨子', '苹果']
# ['苹果', '香蕉', '梨子']
# ['苹果', '梨子', '香蕉']
# ['梨子', '苹果', '香蕉']
# ['梨子', '香蕉', '苹果']

# 全排列 
# 小福利，教你用Python对列表进行全排列组合_littlespider889的博客-CSDN博客
# https://blog.csdn.net/littlespider889/article/details/125827884
