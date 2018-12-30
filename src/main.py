"""
main

@description : execution starts here, sets the
               application and initializes a win-
               dow.
"""

import sys

from PyQt5.QtWidgets import QApplication

from MainController import Controller

from gui.Window import Window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()

    c = Controller(w)

    app.exec()
