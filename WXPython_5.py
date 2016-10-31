# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_5.py
@time: 2016/10/31 10:16
"""
import wx


class Frame(wx.Frame):
    """展示图片"""

    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title="Hello, wxPython"):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


if __name__ == '__main__':
    app = wx.App(False)
    image = wx.Image('wx.jpg', wx.BITMAP_TYPE_JPEG)
    frame = Frame(image)
    frame.Show(True)
    app.MainLoop()
