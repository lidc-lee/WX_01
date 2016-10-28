# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: WXPython_3.py
@time: 2016/10/28 15:22
"""
import wx
import os


class MainWindow(wx.Frame):
    """初始化"""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        # 在file上添加菜单项
        filename = wx.Menu()
        menuAbout = filename.Append(wx.ID_ABOUT, "about", "information about this program")
        filename.AppendSeparator()
        menuExit = filename.Append(wx.ID_EXIT, "exit", "Terminal the program")
        filename.AppendSeparator()
        menuOpen = filename.Append(wx.ID_OPEN, "open", "Terminal the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filename, "file")
        self.SetMenuBar(menuBar)
        # events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        # layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnOpen(self, e):
        """open file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)


app = wx.App(False)
frame = MainWindow(None, "Hello world")
app.MainLoop()
