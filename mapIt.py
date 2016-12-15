# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: mapIt.py
@time: 2016/12/14 11:11
利用webbrowser模块、BeautifulSoup模块、requests模块
"""
import webbrowser
import sys
import requests
import bs4
from selenium import webdriver

url = 'http://inventwithpython.com/'
# webbrowser.open(sys.argv[1])

res = requests.get(url)

print res.status_code
# try:
#     res.raise_for_status()
#     playFile = open('maplt.txt', 'wb')
#     for chunk in res.iter_content(1000):
#         playFile.write(chunk)
#     playFile.close()
#     soupFile = open('text.html')
#     soup = bs4.BeautifulSoup(soupFile, 'html.parser')
#     elems = soup.select('div')
#     type(elems)
#     len(elems)
#     print elems[0].get('class')
#     soupFile.close()
# except Exception as exc:
#     print(exc)

# browser = webdriver.Firefox()
# browser.get(url)
