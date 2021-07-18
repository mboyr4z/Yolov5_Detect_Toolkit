import cv2
from PyQt5 import QtCore,QtGui
import os

def pixmapdonustur(image):      #QLABEL setStyleSheet and setPixmap
    image = QtGui.QImage(image, image.shape[1], \
                         image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(image)
    return pix

def tespitEdilmisVideoyuBas(degiskenler,ui):
    cap = cv2.VideoCapture("runs/detect/" + os.listdir("runs/detect")[-1] + "/video2.mp4")

    while (cap.isOpened()):
        cv2.waitKey(1)
        ret, img = cap.read()

        if ret == True:

            screen = cv2.resize(img, (561, 351))
            pixmap = pixmapdonustur(screen)
            ui.lbl_goruntu.setPixmap(pixmap)

def VideoTespiteBasla(degiskenler,ui):
    if (degiskenler.weightKonum != "" ):
        if (degiskenler.videoKonum != ""):
            os.system('cmd /c "python yolov5-master/detect.py --weights '+degiskenler.weightKonum+' --img 640 --conf 0.25 --source tespitVideo"')
            tespitEdilmisVideoyuBas(degiskenler,ui)



