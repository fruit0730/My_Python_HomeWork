#1.2循环拓展认识
print("奇偶计算器".center(50,"="))
#ls=[1,2,3,4,5,6,7,8,9,0]


def fact():
    print("奇数".center(20,"*"))

    for i in range (len(it)):

        if it[i]%2==1:
            print(it[i])


    print("偶数".center(20,"*"))

    for i in range (len(it)):

        if it[i]%2==0:
            print(it[i])
#
try:
    it = list(map(int, input("请输入数据...\n").split()))

except :
    print("出错了")

fact()
