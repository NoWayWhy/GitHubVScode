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
