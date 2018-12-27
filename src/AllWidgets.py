# ------------------------------------------------PyQt5 imports
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtWidgets import QAction, QVBoxLayout,\
    QToolBar, QLabel, QGridLayout, QWidget
# ------------------------------------------------Other Imports
import ArticleController
# -------------------------------------------------------------
# TODO put actions of layout elem in mainController, not here
# TODO favourites menu
# TODO sourcesEdit menu
# TODO settings menu
# TODO clean code (not priority)


# ===============================================
# Toolbar
# ===============================================
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


# ===============================================
# Home Widget
# ===============================================
from ArticleWidgets import ArticleGridCard


class HomeWidget(QWidget):
    def __init__(self, width_limit, is_first_time):
        super().__init__()
        self.setObjectName("home")

        layout = QGridLayout()

        articles_data = ArticleController.get_article_data()

        for article in articles_data:
            layout.addWidget(ArticleGridCard(QSize(100, 100),
                                             article.images,
                                             article.title,
                                             article.summary,
                                             article.publish_date))

        self.setLayout(layout)


# ===============================================
# Favourites Widget
# ===============================================
class FavouritesWidget(QWidget):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        widget.setObjectName("fav")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from FAVOURITES")

        layout.addWidget(test_label)

        widget.setLayout(layout)


# ===============================================
# Sources Widget
# ===============================================
class SourcesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("src")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from EDIT SOURCES")

        layout.addWidget(test_label)

        self.setLayout(layout)


# ===============================================
# Settings Widget
# ===============================================
class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("sett")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from SETTINGS")

        layout.addWidget(test_label)

        self.setLayout(layout)
