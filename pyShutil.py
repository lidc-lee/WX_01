# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pyShutil.py
@time: 2016/12/8 15:03
shutil 模块--文件的复制、移动删除等
"""
import shutil
import send2trash

import os

# 复制文件
# shutil.copy('text.txt', '.\\lee')
# # 复制文件夹
# shutil.copytree('.\\ldc', 'lee')
# 移动
# shutil.move('.\\lee\\text.txt', '.\\ldc\\ldc.txt')
# 删除文件
# os.unlink('.\\lee\\hello.html')
# 删除文件夹
# os.rmdir('.\\lee')
# 删除文件夹和文件
# shutil.rmtree('lee')

# 安全删除--将文件放到垃圾箱，可以还原
# baconFile = open('text2.txt', 'a')
# baconFile.write('Hello world!!!')
# baconFile.close()
# send2trash.send2trash('text2.txt')

# os.walk()返回当前文件夹的名称的字符串、子文件夹的字符串列表、
# for folderName, subfolders, fileName in os.walk('E:\\study\\pythonStudy\\WX_01\\ldc'):
#     print folderName
#     print subfolders
#     print fileName


