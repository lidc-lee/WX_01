# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pyHanShu.py
@time: 2016/12/8 10:29
函数的使用
"""

# 字符分割
a = "student"
b = a.split("u")
print b


# 自定义函数
# 不带参数
def a():
    print "hello"
    print 777
    print "a"


# 带参数
def test2(i, j):
    k = i * j
    return i, j, k


a()
test = test2(2, 3)
print test
