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
        