from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QAction, QVBoxLayout, QToolBar, QLabel, \
    QGridLayout, QWidget, QSpacerItem, QSizePolicy
import ArticleController


def getMenuToolbar(window):
    toolbar = QToolBar()

    # --------------
    # Toolbar setup
    # --------------
    toolbar.setMovable(False)
    toolbar.setOrientation(Qt.Vertical)
    toolbar.setPalette(QPalette(QColor(30, 30, 30)))
    toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
    toolbar.setIconSize(QSize(64, 64))

    # ----------------------------------
    # Actions setup
    # ----------------------------------

    # QAction(QIcon(. / path / to / file),
    #         name_string, parent=None)

    # home action
    home_act = QAction(QIcon("./assets/icons/home.png"),
                       "home", window)
    home_act.triggered.connect(window.change_widget)

    # favourites action
    fav_act = QAction(QIcon("./assets/icons/favourites.png"),
                      "fav", window)
    fav_act.triggered.connect(window.change_widget)

    # sources action
    src_act = QAction(QIcon("./assets/icons/edit.png"),
                      "src", window)
    src_act.triggered.connect(window.change_widget)

    # settings action
    sett_act = QAction(QIcon("./assets/icons/settings.png"),
                       "sett", window)
    sett_act.triggered.connect(window.change_widget)

    # exit action
    exit_act = QAction(QIcon("./assets/icons/exit.png"),
                       "exit", window)
    exit_act.triggered.connect(window.close)

    # ---------------
    # add to toolbar
    # ---------------
    toolbar.addAction(home_act)
    toolbar.addAction(fav_act)
    toolbar.addAction(src_act)
    toolbar.addAction(sett_act)
    toolbar.addAction(exit_act)

    return toolbar


def getHome():
    widget = QWidget()
    widget.setObjectName("home")
    layout = QGridLayout()

    # articles = ArticleController.get_article_from_source("xd")
    #
    # article_cards = []
    #
    # from ArticleWidgets import ArticleGridCard
    #
    # for article in articles:
    #     article_cards.append(ArticleGridCard())

    # # BEGIN test
    i = 0
    while i < 112:
        for j in range(0, 10):
            label = QLabel("test_label\n number\n   " + str(i))
            # layout.addWidget(label, i, j)
        i += 1
    test_label = QLabel("This is a test from HOME")

    layout.addWidget(test_label)
    # # END test

    widget.setLayout(layout)
    return widget


def getFavourites():
    widget = QWidget()
    widget.setObjectName("fav")
    layout = QVBoxLayout()

    test_label = QLabel("This is a test from FAVOURITES")

    layout.addWidget(test_label)

    widget.setLayout(layout)
    return widget


def getSources():
    widget = QWidget()
    widget.setObjectName("src")
    layout = QVBoxLayout()

    test_label = QLabel("This is a test from EDIT SOURCES")

    layout.addWidget(test_label)

    widget.setLayout(layout)
    return widget


def getSettings():
    widget = QWidget()
    widget.setObjectName("sett")
    layout = QVBoxLayout()

    test_label = QLabel("This is a test from SETTINGS")

    layout.addWidget(test_label)

    widget.setLayout(layout)
    return widget
