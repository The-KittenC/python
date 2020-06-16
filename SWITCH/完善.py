from shutil import copyfile
from sys import exit
import sys
import os
path = os.getcwd()      #获取当前路径
result = []
with open (path + ".\path\path.txt", "r",encoding = "UTF-8") as f:
    for line in f:
        result.append(list(line.strip('\n').split(",")))
print(result[1],result[2])
str1 = "".join(result[1])
str2 = "".join(result[2])
source = str1
target = str2
try:
    copyfile(source, target)
except IOError as e:
    print("无法复制文件" %e)
    exit(1)
except:
    print("意外错误:", sys.exc_info())
    exit(1)

print("复制成功")
print("按任意键退出......")
input()