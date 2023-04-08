# (1-x)^10+x*10=0.5% 

x=0.1
diff=0.03
for i in range(1, 11):
    # x = 0.01*i
    # x = 0.1*i
    # x+=diff
    x-=diff
    # print(x)
    val=(1-x)**10+x*10
    print(val)
    if 0.5/100<val and val<0.5/100+0.0001:
        print(x)
        print(val)
        print(i)
        break
    # print((1-x)**10+x*10)

# res=(1-0.5/100)
print("res")
print((1-0.5/100)**10+0.5/100*10)