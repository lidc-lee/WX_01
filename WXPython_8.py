# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_8.py
@time: 2016/11/2 11:41
对话框
"""
import wx
import sys


class DialogFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(500, 200))
        # dlg = wx.MessageDialog(self, "Is this the coolest thing ever!", "MessageDialog", wx.YES_NO | wx.ICON_QUESTION)
        # result = dlg.ShowModal()
        # dlg.Destroy()
        dlg = wx.TextEntryDialog(parent, "Who is ?", "A question", "Li Dong")
        if dlg.ShowModal() == wx.OK:
            response = dlg.GetValue()
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = DialogFrame(parent=None, title="Dialog")
    frame.Show()
    app.MainLoop()
