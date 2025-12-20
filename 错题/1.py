d = {'A':10, 'B':2, 'C':100, 'D':9, 'E':-10}
s = 0
for i in d:
    if d[i] > 2:
        continue
    s += d[i]  # 只有值不大于2时，才会执行这行
print(s)