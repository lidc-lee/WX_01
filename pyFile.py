# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pyFile.py
@time: 2016/12/8 11:44
文件读写
"""
import os
import shelve

# 创建文件夹
# .当前目录下；..上一级目录下
# os.makedirs('.\\lee')
str = "E:\\study\\python脚本\\WX_01\\text.txt"

path = os.path.join("E:\\study\\python脚本\\WX_01", "text.txt")
# 绝对路径
absPath = os.path.abspath('.\\text.txt')
os.path.isabs('E:\\study\\python脚本\\WX_01')
relpath = os.path.relpath('E:\\study\\python脚本\\WX_01', 'E:\\study')

# 当前目录
os.getcwd()

# 文件名称
basePath = os.path.basename(str)
# 目录名称
dirPath = os.path.dirname(str)
# 分割目录和基本名称
splitpath = os.path.split(str)
str.split(os.path.sep)

# 查看文件大小和内容
size = os.path.getsize('text.txt')
# 该目录下的所有文件
listdir = os.listdir('.')

# 检查有效性
isExist = os.path.exists('E:\\study')
isDir = os.path.isdir('.\\pic\\1.jpg')
isFile = os.path.isfile('text.txt')

# 文件的读写
txtFile = open('text.txt', 'r')
content = txtFile.read()
txtFile.close()

# txt2File = open('text2.txt', 'w')
# # txt2File = open('text2.txt', 'a')
# txt2File.write(content)
# txt2File.close()
#
# txtFile2 = open('text2.txt', 'r')
# content2 = txtFile2.read()
# txtFile2.close()

# shelve 模块保存变量
shelveFile = shelve.open('shelveFile')
cats = ['zophile', 'Pooka', 'Simon']
shelveFile['cats'] = cats

print shelveFile.values()
shelveFile.close()
