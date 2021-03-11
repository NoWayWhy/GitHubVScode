import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtPrintSupport import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(400, 330)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.canvas = Canvas()
        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(self.canvas.clear_drawing)

        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.clear_btn)

class Canvas(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.points = []

        self.resize(400, 330)

    def mouseMoveEvent(self, event):
        self.points.append(event.pos())

        self.update()
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 0))
        for point in self.points:
            p.drawPie(point.x(), point.y(), 10, 10, 0, 180 * 32)
        p.end()
    
    def clear_drawing(self):
        self.points = []
        self.update()
        
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())