import cv2
import os
from PyQt5 import QtCore,QtGui



def WebCamTespiteBasla(degiskenler,ui):
    if (degiskenler.weightKonum != ""):
        os.system('cmd /c "python yolov5-master/detect.py --weights '+degiskenler.weightKonum +' --img 640 --conf 0.25 --source 0"')

