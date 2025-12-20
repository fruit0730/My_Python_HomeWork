#1.7字符炸弹
print("字符炸弹".center(20,"="))
a=(input("此程序非常危险，按Q键退出，按任意键运行"))
if a!="Q".lower():
    with open("example.txt","w",encoding="utf-8") as f:
        for i in range(999999999999999999):
            f.writelines(f"{i}\n")
else:
    exit()