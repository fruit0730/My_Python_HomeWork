# 1.4 文件IO处理
import ReadLiner
def read():
    with open("example.txt", "r", encoding="utf-8") as f:
        f.readline()
        content = f.readline()

        print(content)



def write():
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("ss")
        f.write("aa")


write()
read()