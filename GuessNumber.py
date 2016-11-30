# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: GuessNumber.py
@time: 2016/11/30 15:36
猜数字
"""
import random

secretNumber = random.randint(1, 20)
print("Number between 1 and 20")
for guessTaken in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("too low")
    elif guess > secretNumber:
        print("too high")
    else:
        break
if guess == secretNumber:
    print("Good job!"+str(guess))
else:
    print("No guess")
