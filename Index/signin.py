import sys
import typing
from main import mainApp
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class signinInterface:

    class signin(QMainWindow):

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Sign in")
            self.setGeometry(725, 200, 500, 650)
            self.setMaximumSize(500, 650)
            self.setMinimumSize(500, 650)
            self.setWindowIcon(QIcon('./images/logo_max.png'))
            self.signInTui()

        def signInTui(self):
            self.lable = QLabel('Master password', self)
            self.lable.resize(150, 40)
            self.masterPasswordInput = QLineEdit(self)
            self.masterPasswordInput.move(120, 200)
            self.masterPasswordInput.resize(250, 32)
            self.masterPasswordInput.setStyleSheet("backgroung-color: white")

            self.eneterButton = QPushButton("enter", self)
            self.eneterButton.move(190, 235)
            
            self.eneterButton.clicked.connect(mainApp.App.runMainFunc)

        def runSignin():
            app = QApplication(sys.argv)

            window = signinInterface.signin()
            window.show()

            app.exec()

signinInterface.signin.runSignin()
