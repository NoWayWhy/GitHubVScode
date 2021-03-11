import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("rabbit3.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,255,0))
        p.drawPie(50,150,100,100,0,180*32)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,0,0))
        p.drawPie(50,150,100,100,0,90*32)

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window3()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
