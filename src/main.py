# ----------------- Python3 imports
import sys

# ----------------- PyQt5 imports
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QScrollArea, QMessageBox

# ----------------- Other imports
import AllWidgets
from DataController import PersistentData

"""==============================================
main
@description : execution starts here, sets the 
               application and initializes a win-
               dow.
=============================================="""
# TODO *1
# TODO (from ArticleWidgets) put actions of layout elem here
# TODO modularize main.py (not priority)


# ===============================================
# Main window class
# ===============================================
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        db_controller = PersistentData()

        self.setWindowIcon(QIcon("./assets/icons/app.png"))
        self.setWindowTitle("Article Doge")
        self.move(50, 50)
        self.setFixedSize(800, 600)

        self.init_UI()

    # -------------------------------------------
    # UI setup
    # -------------------------------------------
    def init_UI(self):
        self.main_area = QScrollArea()
        print("further widgets will limited to: " + str(self.main_area.width()))

        toolbar = AllWidgets.Toolbar(self)
        home_widget = AllWidgets.HomeWidget(self.main_area.width(),
                                            is_first_time=True)
        self.main_area.setWidget(home_widget)

        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        self.setCentralWidget(self.main_area)

        self.show()

    # -------------------------------------------
    # Changes window central widget, home, favou-
    # rites, sources or settings.
    #
    # Creates a new instance of the object and
    # gives every layout elem their action.
    # -------------------------------------------
    def change_widget(self):
        widget_name = QObject.sender(self).text()
        current_widget = self.centralWidget().widget().objectName()
        print("widget_name: [" + widget_name +
              "] and current widget: [" + current_widget + "]")
        if widget_name == current_widget:
            print("you already are in " + widget_name)
            # TODO*1 refresh widget if needed (home article feed)
            return

        if widget_name == "home": self._change_to_home_widget()
        elif widget_name == "fav": self._change_to_favourites_widget()
        elif widget_name == "src": self._change_to_sources_widget()
        elif widget_name == "sett": self._change_to_settings_widget()

    def _change_to_home_widget(self):
        home_widget = AllWidgets.HomeWidget(self.main_area.width(),
                                            is_first_time=False)

        for article_card in home_widget.article_cards:
            article_card.clicked.connect(self.show_article)

        self.main_area.setWidget(home_widget)

    def _change_to_favourites_widget(self):
        favourites_widget = AllWidgets.FavouritesWidget()
        self.main_area.setWidget(favourites_widget)

    def _change_to_sources_widget(self):
        widget = AllWidgets.SourcesWidget()

        for edit_source_widget in widget.edit_source_widgets:
            pass
            # TODO

        self.main_area.setWidget(widget)

    def _change_to_settings_widget(self):
        widget = AllWidgets.SettingsWidget()

        # widget.example_setting...... TODO

        self.main_area.setWidget(widget)

    # -------------------------------------------
    # Close confirmation dialog
    # -------------------------------------------
    def closeEvent(self, e):
        e.ignore()
        close = QMessageBox.question(self, "Exiting app",
                                     "Are you sure you want to exit?",
                                     QMessageBox.Yes |
                                     QMessageBox.No)
        if close == QMessageBox.Yes:
            e.accept()

    def __del__(self):
        print(str(self.objectName()) + " is being destroyed... bye")


# ===============================================
# main
# ===============================================
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    app.exec()
