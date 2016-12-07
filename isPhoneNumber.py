# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: isPhoneNumber.py
@time: 2016/12/7 10:16
正则表达式
"""

import re


def isNumber(text):
    str = re.search('(\d\d\d)-(\d\d\d-\d\d\d\d)', text).group(2)
    print(str)


number = "ldc345-456-7888lee234-343-3453"
isNumber(number)
s = re.search(r'Bat(man|mobile|copter|bat)', 'Batman lost a wheel')
print s.group()
s1 = re.search(r'(Batwo)*man', 'Batwoman')
print s1.group()
haRegex = re.search('(Ha){3,5}', 'leeldcHaHaHa')
print(haRegex.group())
print re.findall('\S', '12687hjhjkhhdshcm_#&***%$ \n\t')
print re.findall('[^0-9]', '12709809hdjsakhdjh%@$_')
print re.findall('([A-Za-z0-9])', '12709809hdjsakhdjh%@$_ADYTYY')
print re.findall(r'[aeiouAEIOU]', 'Round of eats baby food .')
print re.search('^(\d+$)', '28945454913232').group(1)
print re.findall('.at', 'cat flat sat hat ')
print re.search('(<.*?>)', '<ldcwweio>leesklp$>').group()
