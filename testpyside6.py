import sys
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import os

env = os.environ
# env.setdefault("QT_DEBUG_PLUGINS","1")
# env.setdefault("QT_QPA_PLATFORM_PLUGIN_PATH", os.getcwd())
env.setdefault("QT_PLUGIN_PATH", os.getcwd())
generated_class, base_class = loadUiType("v1.ui")



class UI(base_class, generated_class):

    checkedimg = 0
    buttons=[]
    labels=[]
    imgs=[]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttons = [self.radioButton_1,self.radioButton_2,self.radioButton_3,self.radioButton_4,self.radioButton_5,self.radioButton_6,self.radioButton_7,self.radioButton_8]
        self.labels = [self.label_pic1,self.label_pic2,self.label_pic3,self.label_pic4,self.label_pic5,self.label_pic6,self.label_pic7,self.label_pic8]

        for b in self.buttons:
            b.clicked.connect(self.img_is_clicked)

        self.searchButton.clicked.connect(self.img_search)

        self.downloadButton.clicked.connect(self.img_download)
        

    def img_is_clicked(self):
        for i,b in enumerate(self.buttons):
            if b.isChecked() : self.checkedimg = i+1

    def img_search(self):
        # 검색어
        print(self.searchbox.toPlainText())

        # 미리보기 이미지 파일 경로를 imgs리스트에 저장 구현 필요
        self.imgs.append("1.png")
        self.imgs.append("2.png")
        self.imgs.append("3.png")
        self.imgs.append("4.png")
        self.imgs.append("5.png")
        self.imgs.append("6.png")
        self.imgs.append("7.png")
        self.imgs.append("8.png")

        self.show_img_to_label()

    def show_img_to_label(self):
        for i in range(8):
            self.labels[i].setPixmap(QPixmap(self.imgs[i]))
            self.labels[i].setScaledContents(True)

    def remove_img_from_label(self):
        for l in self.labels:
            l.setText("image")

    def img_download(self): # 구현 필요
        #self.remove_img_from_label()
        print("이미지 "+str(self.checkedimg)+" 다운로드")



if __name__== "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.show()

    sys.exit(app.exec())