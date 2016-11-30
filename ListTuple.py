# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: ListTuple.py
@time: 2016/11/30 16:39
列表和元组
"""


def test(spam=['apple', 'bananas', 'tofu', 'cats']):
    spam.insert(len(spam) - 1, 'and')
    return spam

print(test())
