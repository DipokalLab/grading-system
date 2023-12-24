
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import QPixmap



MAX_CAPTURE = 2

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grading System v1')
        self.move(300, 300)
        self.resize(1000, 600)

        self.points = []
        self.nowPointCursor = 0

        self.scroll = QScrollArea(self) 
        self.scroll.setGeometry(0,0,500,1000)   

        self.label = QLabel(self)
        self.pixmap = QPixmap('./files/30725-01.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.mousePressEvent = self.getPos

        for i in range(MAX_CAPTURE):
            self.addPointsInput(0, 0)
            self.addPointsInput(0, 0)


        self.scroll.setWidget(self.label) 
        self.show()

    def getPos(self , event):
        x = event.pos().x()
        y = event.pos().y() 
        print(x, y)

        self.points[self.nowPointCursor][1].setText(str(x))
        self.points[self.nowPointCursor][3].setText(str(y))

        self.nowPointCursor += 1



    def addPointsInput(self, x, y):
        lineNumber = len(self.points)

        labelX = QLabel(self)
        labelX.move(540, 20 + (lineNumber * 20))
        labelX.setText('First X :')
        lineX = QLineEdit(str(x), self)
        lineX.move(600, 20 + (lineNumber * 20))

        labelY = QLabel(self)
        labelY.move(740, 20 + (lineNumber * 20))
        labelY.setText('First Y :')
        lineY = QLineEdit(str(y), self)
        lineY.move(800, 20 + (lineNumber * 20))

        self.points.append([labelX, lineX, labelY, lineY])

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Window()
   sys.exit(app.exec_())