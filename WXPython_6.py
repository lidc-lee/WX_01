# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_6.py
@time: 2016/10/31 10:59
<p>添加控件</p>
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Button", pos=wx.DefaultPosition, size=(300, 100))
        panel = wx.Panel(self)  # 创建画板
        button = wx.Button(panel, label="Close", pos=(125, 10), size=(50, 50))
        # 绑定按钮单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        # 绑定窗口关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(parent=None)
    frame.Show(True)
    app.MainLoop()
