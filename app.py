
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import QPixmap



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grading System v1')
        self.move(300, 300)
        self.resize(800, 600)



        self.scroll = QScrollArea(self) 
        self.scroll.setGeometry(0,00,500,1000)   

        self.label = QLabel(self)
        self.pixmap = QPixmap('./files/30725-01.jpg')
        self.pixmap1 = self.pixmap.scaled(1200, 1200, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap1)

        self.scroll.setWidget(self.label) 

        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Window()
   sys.exit(app.exec_())