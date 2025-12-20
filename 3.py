#1.3数据类型综合
print("数据类型综合".center(40,"="))

def 浮点数练习题():
    print('浮点数刁钻练习题'.center(20,'*'))
    a=1.1
    b=1.3
    c=a+b

    if c==2.4 :
        print(True)
    else:
        print(c)
        print(False)


def 字符串练习(strs):
    print('字符串练习题'.center(20, '*'))


    strs1=(strs.center(20,'*'))
    print("centrt方法的作用\n",strs1)

    strs2=strs.upper()
    print("upper方法的作用\n",strs2)

    strs3=strs.lower()
    print("lower方法的作用\n",strs3)

def 其他常用字符串处理方法方法():
    s="How are you doing?"
    d="This is a IPhone for AppleStore"

    print("split方法的作用\n",s.split())         #分隔字符

    print("count方法的作用\n",s.count("o"))      #统计字符出现的次数

    print("replace方法的作用\n",d.replace("IPhone","OPPO Phone"))      #替换字符 new若留空则为删除



def 方法():
    e = "How are you doing?"
    f = "This is a IPhone for AppleStore"
    print(e.join(f))

#浮点数练习题()
#字符串练习(input("请输入文本\n"))
#其他常用字符串处理方法方法()
方法()