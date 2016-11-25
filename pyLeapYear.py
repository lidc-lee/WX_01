# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pyLeapYear.py
@time: 2016/11/24 14:13
闰年
"""


def isLeapYear(year):
    """判断是否为闰年"""
    isFlag = False
    if year % 100 == 0:
        if year % 400 == 0:
            isFlag = True
    elif year % 4 == 0:
        isFlag = True
    return isFlag

if __name__ == '__main__':
    for i in range(1000, 2016):
        if isLeapYear(i):
            print "%d 是闰年"% i
        else:
            print "%d 不是闰年"% i

