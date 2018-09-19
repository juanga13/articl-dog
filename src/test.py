import sys
from newspaper import Article
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QTextEdit
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Gui(QMainWindow):
    screen_state = 0  # 0=main_hub, 1=settings

    def __init__(self, *__args):
        super().__init__(*__args)

        # Main hub widget

        main_hub_widget = QWidget()
        main_hub_layout = QVBoxLayout()
        # upper bar
        upper_bar_layout = QHBoxLayout()
        settings_button = QPushButton("Settings")
        search_box_lineedit = QLineEdit()
        upper_bar_layout.addWidget(settings_button)
        upper_bar_layout.addWidget(search_box_lineedit)
        # article list
        article_scroll_box = QScrollArea()
        article_scroll_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        article_list_layout = QVBoxLayout()
        for i in range(40):
            tmp_button = QPushButton("This is the " + str(i) + " button!")
            tmp_button.setFixedSize(tmp_button.size())
            article_list_layout.addWidget(tmp_button, i)
        article_scroll_box.setLayout(article_list_layout)

        main_hub_layout.addLayout(upper_bar_layout)
        main_hub_layout.addWidget(article_scroll_box)
        main_hub_widget.setLayout(main_hub_layout)
        self.setCentralWidget(main_hub_widget)

        self.setFixedSize(640, 480)
        self.setWindowTitle("Article Dog")
        self.show()


def run():
    url = "https://www.cancilleria.gob.ar/es/actualidad/noticias/fallecimiento-de-jose-manuel-de-la-sota"
    article = Article(url)
    article.download()
    article.parse()
    print(article.title)
    print(article.publish_date)
    print(article.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = Gui()

    sys.exit(app.exec_())
