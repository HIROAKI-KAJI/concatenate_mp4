### check webcam resolution
### $ v4l2-ctl -d /dev/video0 --list-formats-ext

__all__ = ["video_maker"]

import cv2
import time
import os
from datetime import datetime

cordecdic = {
    "mp4":{"fourcc" : 'MJPG',"exts" : ".mp4"}
}

FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
LINE_TYPE=cv2.LINE_AA
FONT_SCALE = 1

class video_maker:
    def __init__(self,output = "",tag = ""):
        self.exportformat = "mp4"
        self.DATA_DIR = output
        self.filetag = tag
        self.size = (960, 540)
        self.FPS = 30
        
        self.filepath = ""
        self.filename = ""
        self.isWriting = False
        self.suddenend = False
        self.life = -1
        
        #self.if not os.path.exists(DATA_DIR):
        #s.mkdir(DATA_DIR)
        
        
    def setfilepath(self):
        self.filename = self.filetag + datetime.now().strftime("%Y%m%d_%H%M%S") + cordecdic[self.exportformat]["exts"]
        self.filepath = os.path.join(self.DATA_DIR ,self.filename)
    def start(self,img):
        self.size = (img.shape[1],img.shape[0])
        self._setup()
    def write(self,img):
        if self.suddenend:
            self.life -= 1
        
        print(self.life)
        if self.isWriting:
            self.videoWriter.write(cv2.resize(img,self.size))
            if self.life == 0:
                self.life = -1
                self.end()
                self.suddenend = False
            
    def _setup(self):
        #self.fourcc = cv2.VideoWriter_fourcc(*cordecdic[self.exportformat]["fourcc"])
        self.fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        
        self.setfilepath()
        self.videoWriter = cv2.VideoWriter(self.filepath, self.fourcc, self.FPS, self.size)
        self.isWriting = True
    
    def end(self,count = -1):
        self.life = count
        if self.life > 0:
            self.suddenend = True
        elif self.isWriting:
            self.isWriting = False
            self.videoWriter.release()
    def __del__(self):
        if self.isWriting:
            self.videoWriter.release()
        

