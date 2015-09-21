#coding=utf-8
import urllib
import re
import wx
import os

app = wx.App()
win = wx.Frame(None,title=u'Spider',size=(400,223))
self = wx.Panel(win)
color = self.SetBackgroundColour('white')

def Create(event):
    path = self.filepath.GetValue()
    os.makedirs(path)
    return path

def getHtmlImg(event):
    path = self.filepath.GetValue()
    name = self.filename.GetValue()
    regop = self.regularop.GetValue()
    reged = self.regulared.GetValue()
    if regop.strip() == '':
        regop = "src="
    url = self.urlpath.GetValue()
    page = urllib.urlopen(url)
    html = page.read()
    reg = r'%s"(.+?)"%s' % (regop,reged)
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    count = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,path + '/%s%d.jpg' % (name,count))
        count += 1

wx.StaticText(self,-1,"Folder:",pos=(5,12))
self.filepath = wx.TextCtrl(self,-1,pos=(50,10),size=(235,25))
createBtn = wx.Button(self,label='Create',pos=(294,10),size=(80,25))
createBtn.Bind(wx.EVT_BUTTON,Create)
wx.StaticText(self,-1,"Name:",pos=(5,47))
self.filename = wx.TextCtrl(self,pos=(50,45),size=(235,25))
wx.StaticText(self,-1,"Regop:",pos=(5,82))
self.regularop = wx.TextCtrl(self,pos=(50,80),size=(235,25))
wx.StaticText(self,-1,"Reged:",pos=(5,117))
self.regulared = wx.TextCtrl(self,pos=(50,117),size=(235,25))
wx.StaticText(self,-1,"Url:",pos=(5,152))
self.urlpath = wx.TextCtrl(self,pos=(50,152),size=(235,25))
getHtmlImgBtn = wx.Button(self,label='DownLoad',pos=(294,152),size=(80,25))
getHtmlImgBtn.Bind(wx.EVT_BUTTON,getHtmlImg)
win.Show()
app.MainLoop()
