from PyQt5.QtCore import QThread, Qt, QSize
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

from src.Layouts import MainHubLayout, ArticlesGetter


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.setFixedSize(800, 600)

        sources = ['https://www.cancilleria.gob.ar/es/actualidad/noticias']
        self.get_articles_thread = ArticlesGetter(sources)

        # self.init_loading_screen()

        main_layout = MainHubLayout(sources)

        self.connect()

    def init_loading_screen(self):
        loading_screen_thread = QThread()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        loading_label = QLabel()
        loading_movie = QMovie("./assets/loading.gif")
        loading_movie.setScaledSize(QSize(600, 600))
        loading_label.setMovie(loading_movie)
        loading_movie.start()

        layout.addWidget(loading_label)

        self.main_widget.setLayout(layout)
