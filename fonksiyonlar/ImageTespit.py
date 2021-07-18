
import cv2
import os
from PyQt5 import QtGui


def pixmapdonustur(image):      #QLABEL setStyleSheet and setPixmap

    image = QtGui.QImage(image, image.shape[1], \
                         image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(image)
    return pix

def tespitEdilmisResmiBas(ui):
    #print("runs/detect/"+os.listdir("runs/detect")[-1]+"/fotograf.png")
    img = cv2.imread("runs/detect/"+os.listdir("runs/detect")[-1]+"/fotograf.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (561, 351))
    pix = pixmapdonustur(img)
    ui.lbl_goruntu.setPixmap(pix)

def imageTespiteBasla(degiskenler,ui):
    if (degiskenler.weightKonum != ""):
        if (degiskenler.imageKonum != ""):

            os.system('cmd /c "python yolov5-master/detect.py --weights '+degiskenler.weightKonum+ ' --img 640 --conf 0.25 --source tespitFotograflar" ')
            tespitEdilmisResmiBas(ui)
        else:
           print("Video ya da Resim Seç")
    else:
        print("Dosya Eksiği")