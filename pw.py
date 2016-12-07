# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pw.py
@time: 2016/12/6 16:42
"""
# ! python2.7
import sys
import pyperclip

passwords = {'email': '1499117534@qq.com', 'name': 'ldc'}

if len(sys.argv) < 2:
    sys.exit()

account = '1499117534@qq.com'
if account in passwords:
    pyperclip.copy(passwords[account])
    print(account)
else:
    print('no account' + account)
