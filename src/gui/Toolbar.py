"""
Toolbar for Main window

@description:
"""

from PyQt5.QtCore import Qt, QSize

from PyQt5.QtGui import QPalette, QColor, QIcon

from PyQt5.QtWidgets import QAction, QToolBar

# TODO doc


class Toolbar(QToolBar):

    def __init__(self, window):
        super().__init__()

        # --------------
        # Toolbar setup
        # --------------
        self.setMovable(False)
        self.setOrientation(Qt.Vertical)
        self.setPalette(QPalette(QColor(30, 30, 30)))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setIconSize(QSize(64, 64))

        # ----------------------------------
        # Actions setup
        # ----------------------------------

        # QAction(QIcon(. / path / to / file),
        #         name_string, parent=None)
        self.home_act = QAction(QIcon("./assets/icons/home.png"),
                                "home", window)
        self.fav_act = QAction(QIcon("./assets/icons/favourites.png"),
                               "fav", window)
        self.src_act = QAction(QIcon("./assets/icons/edit.png"),
                               "src", window)
        self.sett_act = QAction(QIcon("./assets/icons/settings.png"),
                                "sett", window)
        self.exit_act = QAction(QIcon("./assets/icons/exit.png"),
                                "exit", window)

        # ----------------------
        # add actions to toolbar
        # ----------------------
        self.addAction(self.home_act)
        self.addAction(self.fav_act)
        self.addAction(self.src_act)
        self.addAction(self.sett_act)
        self.addAction(self.exit_act)
