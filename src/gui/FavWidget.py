from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

# TODO finish this


class FavWidget(QWidget):
    """===============================================
    Favourites Widget

    @description: menu for Main window. Shows favouri-
                  ted articles.
    =============================================="""

    def __init__(self):
        super().__init__()
        widget = QWidget()
        widget.setObjectName("fav")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from FAVOURITES")

        layout.addWidget(test_label)

        widget.setLayout(layout)

