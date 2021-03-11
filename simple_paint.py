# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_paint.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.clearButton = QPushButton(Form)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(14, 270, 371, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 250, 141, 16))
        self.canvas = QLabel(Form)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setGeometry(QRect(10, 10, 381, 221))
        self.canvas.setAutoFillBackground(False)
        self.canvas.setFrameShape(QFrame.Box)
        self.canvas.setFrameShadow(QFrame.Plain)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Form", u"Drag the mouse to draw", None))
        self.canvas.setText("")
    # retranslateUi

