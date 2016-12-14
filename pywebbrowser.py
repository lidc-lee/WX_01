# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pywebbrowser.py
@time: 2016/12/9 14:55
从web爬取信息
"""
import webbrowser
import requests

# 打开网页
# webbrowser.open('http://www.jikexueyuan.com/path/python')
# 从web下载文件
res = requests.get('http://www.jikexueyuan.com/path/python')
type(res)
print type(res)