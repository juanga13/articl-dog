import sys

from PyQt5.QtWidgets import QApplication

from src.Controller import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)

    controller = Controller()

    app.exec_()
