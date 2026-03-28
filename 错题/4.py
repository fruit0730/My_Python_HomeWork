def f(n):
    s=0
    if s%2!=0:
        for i in range(1, n+1, 2):
            s += 1/i
    else:
        for i in range(2, n+1, 2):
            s += 1/i
    return s
n = int(input())
print(f(n))


#请修改编辑器中的代码，让用户输入一个自然数 n，如果 n 为奇数，输出表达式 1+1/3+1/5+...+1/n 的值；如果 n 为偶数，输出表达式 1/2+1/4+1/6+...+1/n 的值。输出结果保留2位小数。
