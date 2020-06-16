import os
import shutil

file_dir = "C:\\Users\\m1832\\Desktop"
os.chdir(file_dir + "\\w")
print(os.getcwd())
print(os.listdir(os.getcwd()))
os.remove("2.txt")
print(os.listdir(os.getcwd()))
