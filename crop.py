
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QtGui import QPixmap
from PIL import Image
import os


DEBUG_MODE = True
MAX_CAPTURE = 5
PRESET_PAGE = 2
PRESET_PATH = "./preset/"
FILE_EXT = 'jpg'

class CropWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('Grading System v1')
        self.move(300, 300)
        self.resize(1000, 600)

        self.points = []
        self.cropData = [[] for i in range(PRESET_PAGE)] 
        self.isDisableCrop = False
        self.nowPointCursor = 0
        self.nowPageNumber = 1

        self.scroll = QScrollArea(self) 
        self.scroll.setGeometry(0,0,500,600)   

        self.label = QLabel(self)
        self.pixmap = QPixmap(PRESET_PATH + self.getNowFilename())
        self.label.setPixmap(self.pixmap)
        self.label.mousePressEvent = self.getMousePosition

        self.gradingButton = QPushButton(text="Grading", parent=self)
        self.gradingButton.move(680, 540)
        self.gradingButton.setEnabled(False)

        self.cropAllButton = QPushButton(text="Crop All", parent=self)
        self.cropAllButton.move(780, 540)
        self.cropAllButton.setEnabled(False)
        self.cropAllButton.clicked.connect(self.cropAllImage)

        


        if (PRESET_PAGE > 1):
            self.nextPageButton = QPushButton(text="Next Page", parent=self)
            self.nextPageButton.move(880, 540)
            self.nextPageButton.clicked.connect(self.setNextPage)

        for i in range(MAX_CAPTURE):
            self.addPointsInput(0, 0)
            self.addPointsInput(0, 0)


        self.scroll.setWidget(self.label) 
        self.show()


    def getMousePosition(self , event):
        if (self.isDisableCrop):
            return True
        
        x = event.pos().x()
        y = event.pos().y() 
        filename = self.getNowFilename()

        if (DEBUG_MODE):
            print(x, y)

        self.points[self.nowPointCursor][1].setText(str(x))
        self.points[self.nowPointCursor][3].setText(str(y))
        self.points[self.nowPointCursor][4] = filename

        self.nowPointCursor += 1

        if (self.nowPointCursor >= MAX_CAPTURE * 2):
            self.getCropImage()
            self.nextPageButton.setEnabled(False)
            self.cropAllButton.setEnabled(True)
            self.isDisableCrop = True


    def getCropImage(self):
        for i in range(0, MAX_CAPTURE * 2, 2):
            filename = self.points[i][4]
            print(filename)

            img = Image.open(PRESET_PATH + filename)
            imgMinX = int(self.points[i][1].text())
            imgMinY = int(self.points[i][3].text())
            imgMaxX = int(self.points[i+1][1].text())
            imgMaxY = int(self.points[i+1][3].text())
            imageNumber = self.getPageNumberFromFilename(filename)

            self.cropData[imageNumber - 1].append([imgMinX, imgMinY, imgMaxX, imgMaxY])

            imgCropped = img.crop((imgMinX, imgMinY, imgMaxX, imgMaxY))
            if (DEBUG_MODE):
                imgCropped.show()

    def getPageNumberFromFilename(self, filename):
        page = int(filename.split(".jpg")[0].split("-")[1])
        return page

    def setNextPage(self):
        self.nowPageNumber += 1
        self.changePreviewImage()
        # print(self.nowPageNumber)

    def getNowFilename(self):
        filename = "preset-{:02d}.{ext}".format(self.nowPageNumber, ext=FILE_EXT)
        return filename

    def changePreviewImage(self):
        filename = self.getNowFilename()
        fileUrl = PRESET_PATH + filename
        self.pixmap = QPixmap(fileUrl)
        self.label.setPixmap(self.pixmap)
        self.scroll.setWidget(self.label) 

        
    def cropAllImage(self):
        path = './files/'
        filelist = os.listdir(path)
        count = 0

        for filename in filelist:
            targetPageNumber = self.getPageNumberFromFilename(filename)
            
            for data in self.cropData[targetPageNumber - 1]:
                imgMinX = data[0]
                imgMinY = data[1]
                imgMaxX = data[2]
                imgMaxY = data[3]

                img = Image.open(path + filename)
                imgCropped = img.crop((imgMinX, imgMinY, imgMaxX, imgMaxY))
                # imgCropped.show()
                imgCropped.save("./result/" + "{:02d}-{filename}".format(count, filename=filename))
                count += 1




    def addPointsInput(self, x, y):
        lineNumber = len(self.points)
        filename = self.getNowFilename()


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

        self.points.append([labelX, lineX, labelY, lineY, filename])
