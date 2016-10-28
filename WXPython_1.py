# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_1.py
@time: 2016/10/28 15:08
"""
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)
app.MainLoop()
