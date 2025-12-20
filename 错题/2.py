def func(x = [], y = [6,7]):
    x.append(8)
    y.append(8)
    return(x+y)

print("1. 函数定义时默认参数:")
print(f"   默认x的id: {id(func.__defaults__[0])}, 值: {func.__defaults__[0]}")
print(f"   默认y的id: {id(func.__defaults__[1])}, 值: {func.__defaults__[1]}")

a, b = [1,2], [3,4]

print("\n2. 第一次调用: t = func(x=a)")
t = func(x=a)
print(f"   修改后a: {a}")
print(f"   默认y被修改为: {func.__defaults__[1]}")

print("\n3. 第二次调用: t = func(y=b)")
t = func(y=b)
print(f"   修改后b: {b}")
print(f"   默认x被修改为: {func.__defaults__[0]}")
print(f"   默认y现在是: {func.__defaults__[1]}")

print("\n4. 第三次调用: print(func())")
result = func()
print(f"   结果: {result}")