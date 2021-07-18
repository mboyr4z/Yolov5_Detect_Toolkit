#python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/

# if __name__ == "__main__":
#     os.chdir("Yolov5_Detect_Toolkit/yolov5-master")
#     os.system('cmd /c "python detect.py --weights ../last.pt --img 640 --conf 0.25 --source ../val"')
import os

from PyQt5 import QtWidgets
from degiskenler.degiskenler import degiskenClass
from design.tasarim import Ui_Form
from fonksiyonlar.ImageTespit import *
from fonksiyonlar.WebCamTespit import *
from fonksiyonlar.DosyaKonumBulma import *
from fonksiyonlar.VideoTespit import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # NESNE TANIMLAMALARIM
    degiskenler = degiskenClass()
    ui = Ui_Form()

    #TIKLANMA OLAYLARIM
    ui.btn_weight.clicked.connect(lambda :  weightKonumBulma(degiskenler,ui))

    ui.btn_image.clicked.connect(lambda: imageKonumBulma(degiskenler, ui))
    ui.btn_video.clicked.connect(lambda: videoKonumBulma(degiskenler, ui))

    ui.btn_imageBasla.clicked.connect(lambda: imageTespiteBasla(degiskenler,ui))
    ui.btn_videoBasla.clicked.connect(lambda: VideoTespiteBasla(degiskenler,ui))
    ui.btn_webCamBasla.clicked.connect(lambda: WebCamTespiteBasla(degiskenler,ui))


    sys.exit(app.exec_())