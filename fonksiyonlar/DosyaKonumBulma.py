
from tkinter import filedialog
import cv2
from PyQt5 import QtGui
from tkinter import *
import shutil


root = Tk()
root.withdraw()

def pixmapdonustur(image):      #QLABEL setStyleSheet and setPixmap
    image = QtGui.QImage(image, image.shape[1], \
                         image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(image)
    return pix

def weightKonumBulma(degiskenler,ui):
    degiskenler.weightKonum = filedialog.askopenfilename()

    if(degiskenler.weightKonum != ""):
        ui.btn_weight.setText("Weight Seçili")

def imageKonumBulma(degiskenler,ui):
    degiskenler.imageKonum = filedialog.askopenfilename()
    if (degiskenler.imageKonum != ""):
        img = cv2.imread(degiskenler.imageKonum)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite("tespitFotograflar/fotograf.png", img)

        img = cv2.resize(img, (561, 351))

        pix = pixmapdonustur(img)
        ui.lbl_goruntu.setPixmap(pix)
        ui.btn_image.setText("Image Seçili")

def videoKonumBulma(degiskenler,ui):
    degiskenler.videoKonum = filedialog.askopenfilename()

    if (degiskenler.videoKonum != ""):
        ui.btn_video.setText("Video Seçili")

        gecici = str(degiskenler.videoKonum)
        gecici = gecici.replace("/",r"\\")
        shutil.copy(gecici, "tespitVideo/")









