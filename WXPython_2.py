# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_2.py
@time: 2016/10/28 15:14
"""
import wx


class MyFrame(wx.Frame):
    """初始化"""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None, "Small editor")
app.MainLoop()
