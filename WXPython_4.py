# -*-coding:utf-8-*-

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_4.py
@time: 2016/10/31 9:25
<p>创建一个文本框的窗口来显示鼠标的位置</p>
"""
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        """wxpython 中文前加u"""
        wx.Frame.__init__(self, None, -1, u"我的", size=(300, 300))
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
