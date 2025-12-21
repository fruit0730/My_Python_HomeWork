text = "National Computer Rank Examination"
Chart = {"小明": 79, "小红": 83}


def bin():
    print("考试名称{1}{0}".format(text, "是这样的"))


def main():
    print("{:=^50}\n{:=^48}".format(text, "Python成绩查询系统"))

    name = input("请输入姓名: ")

    # 检查姓名是否在字典中
    if name in Chart:
        # 正确访问字典值并格式化输出
        print(f"{name}的成绩为：\n{Chart[name]}分")
    else:
        print(f"找不到学生'{name}'的成绩")


# 调用函数
bin()  # 调用第一个函数
print()  # 空行
main()  # 调用主函数