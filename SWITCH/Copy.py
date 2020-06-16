from shutil import copyfile
from sys import exit

source = input("源文件地址: ")
target = input("目标文件地址: ")

try:
    copyfile(source, target)
except IOError as e:
    print("无法复制文件" %e)
    exit(1)
except:
    print("意外错误:", sys.exc_info())
    exit(1)

print("复制成功")