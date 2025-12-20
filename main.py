import subprocess
import sys


def run_python_program():
    """运行Python程序"""
    filename = input("请输入要运行的Python文件名: ")

    if not filename.endswith('.py'):
        filename += '.py'

    try:
        # 运行Python程序
        result = subprocess.run([sys.executable, filename],
                                text=True)

        print(f"\n程序运行结束")

    except FileNotFoundError:
        print(f"错误: 找不到文件 '{filename}'")
    except Exception as e:
        print(f"运行出错: {e}")

#
# 直接运行
run_python_program()