# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: bulletPointAdder.py
@time: 2016/12/6 17:07
"""
import pyperclip
pyperclip.copy('List of animals\nList of animals\n List of animals\n  ')
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

pyperclip.copy(text)
