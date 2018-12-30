"""

"""

import urllib

from PyQt5.QtGui import QImage, QPixmap, QPalette, QBrush

from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

# TODO doc


class ArtlGridCard(QWidget):
    """

    """

    def __init__(self, q_size, photo_path, title, description, date):
        super().__init__()

        print("creating new article card")

        self.photo_path = photo_path
        self.title = title
        self.description = description
        self.date = date

        self.setFixedSize(128, 128)

        self.init_ui(q_size)

    # -------------------------------------------
    # UI components init, takes size and defines
    # its scale.
    # -------------------------------------------
    def init_ui(self, q_size):
        layout = QVBoxLayout()

        title_text = QLabel(self.title)
        title_text.setWordWrap(True)
        description_text = QLabel(self.description)
        description_text.setWordWrap(True)

        layout.addWidget(title_text)
        layout.addWidget(description_text)

        image_data = urllib.request.urlopen(self.photo_path).read()
        image = QImage()
        image.loadFromData(image_data)

        background = QPixmap(image)

        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(background))
        self.setPalette(palette)

        self.setLayout(layout)

