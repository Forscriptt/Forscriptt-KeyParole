import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class mainApp:
    class App(QMainWindow):

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Forscriptt Key Parole")
            self.setGeometry(325, 140, 1250, 750)
            self.setWindowIcon(QIcon('./images/logo_max.png'))

        def runMainFunc():
            app = QApplication(sys.argv)

            window = mainApp.App()
            window.show()

            app.exec()
