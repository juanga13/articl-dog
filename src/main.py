# Python3 imports
import sys

# PyQt5 imports
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QHBoxLayout, QScrollArea, QGridLayout, QLabel, \
    QWidget, QDialog, QMessageBox

# Other imports
import AllWidgets

"""
main
@description : execution starts here, sets the 
               application and initializes a win-
               dow.
"""
# NOTODO


# ===============================================
# Main window class
# ===============================================
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 600, 400)

        self.init_UI()

    # -------------------------------------------
    # UI setup
    # -------------------------------------------
    def init_UI(self):
        toolbar = AllWidgets.getMenuToolbar(self)
        home_widget = AllWidgets.getHome()

        main_area = QScrollArea()
        main_area_layout = QGridLayout()
        main_area.setLayout(main_area_layout)

        main_area_layout.addWidget(home_widget)

        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        self.setCentralWidget(main_area)

        self.show()

    # -------------------------------------------
    # Close confirmation dialog
    #
    # @description : this a slot for the toolbar
    #                actions.
    # -------------------------------------------
    def change_widget(self):
        widget_name = QObject.sender(self).text()
        if widget_name is self.centralWidget().objectName():
            print("widget is current, bye")
            return

        print("sender is: [" + str(widget_name) + "]")

        if widget_name == "home":
            home_widget = AllWidgets.getHome()
            self.setCentralWidget(home_widget)

        elif widget_name == "fav":
            print("clicked on fav, so changing to fav widget")
            favourites_widget = AllWidgets.getFavourites()
            self.setCentralWidget(favourites_widget)

        elif widget_name == "src":
            sources_widget = AllWidgets.getSources()
            self.setCentralWidget(sources_widget)

        elif widget_name == "sett":
            settings_widget = AllWidgets.getSettings()
            self.setCentralWidget(settings_widget)

    # -------------------------------------------
    # Close confirmation dialog
    # -------------------------------------------
    def closeEvent(self, e):
        e.ignore()
        if QMessageBox.Yes == QMessageBox.question(self, "QUIT", "Sure?",
                                                   QMessageBox.Yes |
                                                   QMessageBox.No):
            e.accept()


# ===============================================
# main
# ===============================================
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    app.exec()
