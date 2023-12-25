
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import QPixmap
from PIL import Image

from crop import CropWindow
from grading import GradingWindow


DEBUG_MODE = True
MAX_CAPTURE = 3
PRESET_PAGE = 2
FILE_EXT = 'jpg'

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grading System v1')
        # self.move(300, 300)
        self.resize(1000, 600)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(0,0,1000,600) 
        # self.stackedWidget.setFrameShape(QFrame.Box) 

        self.crop = CropWindow()
        self.stackedWidget.addWidget(self.crop)
        self.crop.gradingButton.clicked.connect(self.goMaker)

        self.maker = GradingWindow()
        self.stackedWidget.addWidget(self.maker)

        self.stackedWidget.setCurrentIndex(0)

        print(self.stackedWidget.count())


    def goMaker(self):
        self.stackedWidget.setCurrentIndex(1)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Window()
   ex.show()
   sys.exit(app.exec_())