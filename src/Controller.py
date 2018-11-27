import newspaper
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QGroupBox
from newspaper import Article

from src.Layouts import Layouts


class ArticlesGetter(QThread):

    def __init__(self, url):
        super().__init__()

        # self.url = url
        self.url = "https://www.cancilleria.gob.ar/es/actualidad/noticias/"

    def __del__(self):
        self.wait()

    def _get_article_data(self, article_url):
        article = Article(article_url)
        article.download()
        article.parse()
        print(article.title)
        print(article.publish_date)
        print(article.text)

    def run(self):
        cancilleria_gov = newspaper.build(self.url)
        for article in cancilleria_gov.article_urls():
            if str(article).startswith(self.url):
                print(str(article) + " is good, adding to list.")
                self.emit(pyqtSignal("add_article(Article)", self._get_article_data(str(article))))
            else:
                print("ignoring " + str(article) + " as its not good.")


class Window(QMainWindow):

    def __init__(self, flags, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.setFixedSize(800, 600)

        self.init_loading_screen()


class MainHubLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()

        self.get_articles_thread = ArticlesGetter(url="foo")

        self.connect(self.get_articles_thread, pyqtSignal("add_post(Article)"), self.add_article)

    def add_article(self, article):

        article_groupbox = QGroupBox(article.title)
        article_groupbox_layout = QVBoxLayout()

        # article_description()

        article_groupbox_layout.addWidget()

        article_groupbox.setLayout(article_groupbox_layout)

        self.addWidget(article_groupbox)


class Controller:

    def __init__(self):

        self.window = Window()

        self.window.show()

        self.init_layout()

    def init_loading_screen(self):

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        loading_label = QLabel()
        loading_movie = QMovie("./assets/loading.gif")
        loading_movie.setScaledSize(QSize(600, 600))
        loading_label.setMovie(loading_movie)
        loading_movie.start()

        layout.addWidget(loading_label)

        self.main_widget.setLayout(layout)

    async def init_layout(self):

        layouts = Layouts()

        self.main_widget.setLayout(layouts.layout_dict["Main Hub"])
