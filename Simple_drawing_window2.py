import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit2.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))

        p.setPen(QColor(255,255,125))
        p.setBrush(QColor(255,255,0))
        p.drawPie(50,150,100,100,0,180*27)

        p.setBrush(QColor(0,0,0))
        p.drawPie(90,170,20,20,0,180*32)

        p.setBrush(QColor(255,127,0))
        p.drawPie(160,230,20,20,0,180*32)

        p.drawPie(270,310,20,20,0,180*32)

        p.drawPie(380,390,20,20,0,180*32)

        p.drawPixmap(QRect(300,60,200,200),self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
