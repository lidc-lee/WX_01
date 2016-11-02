# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_7.py
@time: 2016/11/2 10:53
<p>给框架增加菜单栏、工具栏、状态栏
"""
import wx


class ToolBarFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Toolbar", size=(300, 300))
        image = wx.Image('wx.jpg', wx.BITMAP_TYPE_JPEG)
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolBar = self.CreateToolBar()
        # toolBar.AddSimpleTool(wx.NewId())
        toolBar.Realize()

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "copy in status bar")
        menu2.Append(wx.NewId(), "&Cut", "")
        menu2.Append(wx.NewId(), "&Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "Options...", "Display options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)


if __name__ == '__main__':
    app = wx.App()
    frame = ToolBarFrame(parent=None)
    frame.Show(True)
    app.MainLoop()
