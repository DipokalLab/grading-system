
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class GradingWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setWindowTitle('Grading System v1')
        self.move(300, 300)
        self.resize(1000, 600)



