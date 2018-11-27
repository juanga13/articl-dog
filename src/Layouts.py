import newspaper
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QLabel
from newspaper import Article


class ArticlesGetter(QThread):

    def __init__(self, sources):

        super().__init__()
        self.sources = sources

    def __del__(self):

        self.wait()

    def run(self):

        for url in self.sources:
            build = newspaper.build(url, memorize_articles=False)
            for article in build.articles:
                if str(article.url).startswith(url):
                    self.emit(article)


class MainHubLayout(QVBoxLayout):

    def __init__(self, sources):
        super().__init__()

        self.get_articles_thread = ArticlesGetter(sources)
        # (self.get_articles_thread, pyqtSignal("add_post(Article)"), self.add_article)
        self.get_articles_thread.connect(self.add_article)
        # pyqtSignal(self.get_articles_thread, self.add_article)

    def add_article(self, article):
        article.download()
        article.parse()

        article_groupbox = QGroupBox(article.title)
        # article_groupbox.clicked.connect(pyqtSignal(""), article)

        article_groupbox_layout = QVBoxLayout()

        article_publisheddate_label = QLabel(article.publish_date)
        article_description_label = QLabel(article.summary)

        article_groupbox_layout.addWidget(article_publisheddate_label)
        article_groupbox_layout.addWidget(article_description_label)

        article_groupbox.setLayout(article_groupbox_layout)

        self.addWidget(article_groupbox)


class ArticleTab(QVBoxLayout):

    def __init__(self, article):
        super().__init__()

        self.article = article

        title_label = QLabel(article.title)
        publishdate_label = QLabel(article.publish_date)
        authors_label = QLabel(article.authors)
        text_label = QLabel(article.text)
        text_label.setWordWrap(True)

        self.addWidget(title_label)
        self.addWidget(publishdate_label)
        self.addWidget(authors_label)
        self.addWidget(text_label)
