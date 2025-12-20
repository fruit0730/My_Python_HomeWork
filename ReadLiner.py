#Python中可以规定读取行数的一个模块
#By Ling

def readliner(t,n):
    with open(t, "r", encoding="utf-8") as f:
        # 读取所有行，然后取第n行
        all_lines = f.readlines()
        if len(all_lines) >= n:
            return all_lines[n-1].strip()  # 索引从0开始
        else:
            return None