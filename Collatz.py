# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: Collatz.py
@time: 2016/11/30 15:57

"""

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

num = int(input())
res = collatz(num)
while res != 1:
    res = collatz(res)


