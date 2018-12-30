"""
Window

main ui where the rest of widgets and layouts
converges.
"""

from PyQt5.QtCore import Qt, QObject

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMainWindow, \
    QScrollArea, QMessageBox

from datamanagement.PermDataController \
    import PermDataController

from gui.HomeWidget import HomeWidget

from gui.FavWidget import FavWidget

from gui.SrcWidget import SrcWidget

from gui.SettWidget import SettWidget

from gui.Toolbar import Toolbar


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        db_controller = PermDataController()

        self.setWindowIcon(QIcon("./assets/icons/app.png"))
        self.setWindowTitle("Article Doge")
        self.move(50, 50)
        self.setFixedSize(800, 600)

        self.init_UI()

    # -----------------------------------------------
    # UI setup
    # -----------------------------------------------
    def init_UI(self):
        self.main_area = QScrollArea()
        print("further widgets will limited to: "
              + str(self.main_area.width()))

        toolbar = Toolbar(self)
        home_widget = HomeWidget(self.main_area.width(),
                                 is_first_time=True)
        self.main_area.setWidget(home_widget)

        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        self.setCentralWidget(self.main_area)

        self.show()

    # -----------------------------------------------
    # Changes window central widget, home, favouri-
    # tes, sources or settings.
    #
    # Creates a new instance of the object and gives
    # every layout elem their action.
    # -----------------------------------------------
    def change_widget(self):
        widget_name = QObject.sender(self).text()
        current_widget = self.centralWidget().widget().objectName()
        print("widget_name: [" + widget_name +
              "] and current widget: [" + current_widget + "]")
        if widget_name == current_widget:
            print("you already are in " + widget_name)
            # TODO*1 refresh widget if needed (home article feed)
            return

        if widget_name == "home":
            self._change_to_home_widget()
        elif widget_name == "fav":
            self._change_to_favourites_widget()
        elif widget_name == "src":
            self._change_to_sources_widget()
        elif widget_name == "sett":
            self._change_to_settings_widget()

    def _change_to_home_widget(self):
        home_widget = HomeWidget(self.main_area.width(),
                                 is_first_time=False)

        for article_card in home_widget.article_cards:
            article_card.clicked.connect(self.show_article)

        self.main_area.setWidget(home_widget)

    def _change_to_favourites_widget(self):
        favourites_widget = FavWidget()
        self.main_area.setWidget(favourites_widget)

    def _change_to_sources_widget(self):
        widget = SrcWidget()

        for edit_source_widget in widget.edit_source_widgets:
            pass
            # TODO

        self.main_area.setWidget(widget)

    def _change_to_settings_widget(self):
        widget = SettWidget()

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
