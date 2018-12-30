"""===============================================
Home Widget

@description: menu for Main window
=============================================="""

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QWidget, QGridLayout

import ArticleController

# TODO doc


class HomeWidget(QWidget):

    def __init__(self, width_limit, is_first_time):
        super().__init__()
        self.setObjectName("home")

        layout = QGridLayout()

        artl_data = ArticleController.get_article_data()

        for artl in artl_data:
            a = ArticleGridCard(QSize(100, 100),
                                artl.images,
                                artl.title,
                                artl.summary,
                                artl.publish_date)
            layout.addWidget(a)
        self.setLayout(layout)
