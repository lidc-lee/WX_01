# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: xinlanlogin.py
@time: 2016/12/13 14:55
"""
import requests

url = 'http://weibo.cn/u/1890493665'  # 此处请修改为微博地址
url_login = 'https://login.weibo.cn/login/'

html = requests.get(url).content
