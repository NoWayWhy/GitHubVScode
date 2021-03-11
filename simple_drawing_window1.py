import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit1.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(242, 222, 222))
        p.setBrush(QColor(242, 222, 222))
        p.drawPie(50,100,100,100,0,180*32)

        p.setPen(QColor(254, 204, 0))
        p.setBrush(QColor(254, 204, 0))
        p.drawPie(50,150,100,100,0,180*32)
        
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())