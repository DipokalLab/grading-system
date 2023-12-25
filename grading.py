
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap




class GradingWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('Grading System v1')
        self.move(300, 300)
        self.resize(1000, 600)

        filelist = os.listdir('./result')

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(filelist))
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        for i in range(len(filelist)):
            label = QLabel(self)
            pic = QPixmap("./result/" + filelist[i])
            pic = pic.scaledToWidth(500)
            label.setPixmap(pic)

            # self.tableWidget.setItem(i, 0, QTableWidgetItem("S"))

            self.tableWidget.setCellWidget(i, 0, label)

            # self.tableWidget.setImage(i, 1, "./result/" + filelist[i])

            # for j in range(3):


        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


