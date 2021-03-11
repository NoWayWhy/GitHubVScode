import sys
import PySide6.QtCore import *
import PySide6.QtWidgets import *
import PySide6.QtGui import *

class simple_drawing_window1(QtWidgets):
    def __init__(self):
        QtWidgets.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixMap("image/rabbit.png")