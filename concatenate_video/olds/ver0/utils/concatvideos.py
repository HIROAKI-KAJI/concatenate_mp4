
import cv2
import os

from utils import video_maker



class concatvideos:
    readablelist = [".mp4"]
    def __init__(self):
        self.exportfolder = os.getcwd()
    def setvideowriter(self,pathlist):
        for p in pathlist:
            if self.pathcheck(p):
                movie = cv2.VideoCapture(p)
                ret, frame = movie.read()
                self.videomaker.start(frame)
                break
            else:
                pass
    def export(self,pathlist,outpath):
        self.videomaker = video_maker.video_maker(output = outpath)
        self.setvideowriter(pathlist)
        
        for path in pathlist:
            if self.pathcheck(path):
                print(path)
                self.writevideo(path)
            else:
                pass
        self.videomaker.end()
    def writevideo(self,path):
        movie = cv2.VideoCapture(path)

        if movie.isOpened() == True: 
            ret, frame = movie.read() 
        else:
            print("VIDEO LOAD EROOR CAN NOT OPEN {path}".format(path))
            ret = False

        while ret:
            self.videomaker.write(frame)
            ret, frame = movie.read()
    
            
    def pathcheck(self,path):
        if(os.path.exists(path)):
            bace, ext = os.path.splitext(path)
            if ext in self.readablelist:
                return True
            else:
                print("PATH ERORR DIFFERENT EXTENSION {}".format(ext))
                return False
        else:
            print("PATH ERORR NOT EXIST {}".format(path))
            return False
            
