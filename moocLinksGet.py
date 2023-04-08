

linkArticle="""
1237071659
1237072629
1237068750
1237068752
1237070693
1237069773
1237072630
1237068753
1237067810
1237071660"""

import listUtil

links=listUtil.str_rets_kind_to_list(linkArticle)
print(links)
"""
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237071659
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237072629
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237068750
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237068752
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237070693
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237069773
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237072630
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237068753
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237067810
https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237071660
"""

linksAll=[]
for linkContentId in links:
    # print(i)
    link=f"https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id={linkContentId}"
    print(link)
    linksAll.append(link)


print(linksAll)
"""
['https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237071659', 'https://www.icourse163.org/learn/HIT-15
4005?tid=1463162470#/learn/hw?id=1237072629', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=12370687
50', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237068752', 'https://www.icourse163.org/learn/HI
T-154005?tid=1463162470#/learn/hw?id=1237070693', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237
069773', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237072630', 'https://www.icourse163.org/lear
n/HIT-154005?tid=1463162470#/learn/hw?id=1237068753', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=
1237067810', 'https://www.icourse163.org/learn/HIT-154005?tid=1463162470#/learn/hw?id=1237071660']
"""