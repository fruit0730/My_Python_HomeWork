#1.1递归练习

def factorial(n):
    try:
        if n==0 :
            return 1
        else:
            return n * factorial(n-1)
    except :
        return "出错了"

try:
    n=int(input("please input a number,only integer:"))
    print(factorial(n))
#
except :
    print("出错了")


