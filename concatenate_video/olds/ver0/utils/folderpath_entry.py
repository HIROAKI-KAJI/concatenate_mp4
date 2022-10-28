""" entry and fildialog button frame object

"""

from tkinter import *
from tkinter import filedialog

__all__ = ["folderpath_entry"]


class folderpath_entry(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        self.text = StringVar()
        self.text.set("")
        
        self._setwidgets()
    def _setwidgets(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=3, minsize=270)
        self.grid_columnconfigure(1, weight=0, minsize=30)
        
        self.entry = Entry(self,textvariable = self.text)
        self.button = Button(self,text = "getpath",command = self.GetFolderPath)
        
        self.entry.grid(row = 0,column = 0,sticky = N+E+W+S)
        self.button.grid(row = 0,column = 1,sticky = N+E+W+S)
    def get(self):
        return self.text.get()
    def GetFolderPath(self):
        current_dir = 'C:\\pg'
        WorkDir = filedialog.askdirectory(initialdir=current_dir)
        self.text.set(WorkDir)
    def disable(self):
        self.entry['state'] = DISABLED
        self.button['state'] = DISABLED
    def able(self):
        self.entry['state'] = NORMAL
        self.button['state'] = NORMAL
