import os
import tkinter as tk
from tkinterdnd2 import *


from utils import concatvideos as CTV
from utils import folderpath_entry

try:
    from Tkinter import *
    from ScrolledText import ScrolledText
except ImportError:
    from tkinter import *
    from tkinter.scrolledtext import ScrolledText



def drop(event):
    if event.data:
        print('Dropped data:\n', event.data)
        #print_event_info(event)
        if event.widget == listbox:
            
            files = listbox.tk.splitlist(event.data)
            for f in files:
                if os.path.exists(f):
                    print('Dropped file: "%s"' % f)
                    listbox.insert('end', f)
                else:
                    print('Not dropping file "%s": file does not exist.' % f)
        else:
            print('Error: reported event.widget not known')
    return event.action

class PropertyFrame(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.texts = list()
        
        tlist = ["drag and drop mp4 file in left box","export button is under this explanation","push export button then start concatenating wideos and rewrite video to export"]
        self._settext(tlist)
        self._setwidgets()
        
    def _setwidgets(self):
        self.textwidget = list()
        rownum = 0
        for t in self.texts:
            self.textwidget.append(tk.Label(self,text = t,anchor = tk.W))
            self.textwidget[-1].grid(row = rownum,column = 0,sticky = tk.N+tk.W+tk.S+tk.E)
            rownum +=1
        
        
    def _settext(self,textlist):
        self.texts = textlist

def export():
    videolist = list(listbox.get(0,tk.END))
    
    Ctv = CTV.concatvideos()
    outfilepath = FolderE.get()
    if(os.path.exists(outfilepath)):
    	Ctv.export(videolist,outfilepath)
    else:
        print("Please set the output destination")
def delist():
    listbox.delete(0, tk.END)
    
def inputbind():
    id = listbox.dnd_bind('<<Drop>>', drop)
    listbox.id = id
def unable():
    listbox.unbind('<<Drop>>',listbox.id)
    listbox['state'] = tk.DISABLED
    DButton['state'] = tk.DISABLED
    exportB['state'] = tk.DISABLED
    FolderE.disable()
def able():
    inputbind()
    listbox['state'] = tk.NORMAL
    DButton['state'] = tk.NORMAL
    exportB['state'] = tk.NORMAL
    FolderE.able()
    
if __name__ == '__main__':
    root = TkinterDnD.Tk()
    
    root.title('TkinterDnD demo')
    root.grid_rowconfigure(2, weight=1, minsize=250)
    root.grid_columnconfigure(0, weight=1, minsize=300)
    root.grid_columnconfigure(1, weight=1, minsize=300)
    
    
    label_1 = tk.Label(root,text = "video import")
    
    listbox = tk.Listbox(root, name='dnd_listbox',selectmode='extended', width=1, height=1)
    listbox.drop_target_register(DND_FILES, DND_TEXT)
    
    DButton = tk.Button(root,text = "list clear",command = delist)
    
    label_2 = tk.Label(root,text = "property")
    FolderE = folderpath_entry.folderpath_entry(root)
    proptyF = PropertyFrame(root)
    exportB = tk.Button(root,text = "export",command = export)
    
    label_1.grid(row = 0,column = 0)
    listbox.grid(row = 1,column = 0,rowspan = 3,padx=5, pady=5, sticky='news')
    DButton.grid(row = 4,column = 0)
    
    label_2.grid(row = 0,column = 1)
    FolderE.grid(row = 1,column = 1,padx = 5,pady = 3,sticky = 'news')
    proptyF.grid(row = 2,column = 1,padx = 5,pady = 5,sticky = 'news')
    exportB.grid(row = 4,column = 1)
    
    inputbind()
    root.mainloop()
