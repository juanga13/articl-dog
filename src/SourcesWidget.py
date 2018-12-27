from PyQt5.QtGui import QImage, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton


class EditSourceWidget(QWidget):
    def __init__(self, url):
        super().__init__()

        layout = QHBoxLayout()

        self.url_edit = QLineEdit(url)
        self.del_button = QPushButton()

        # set button image (palette)
        del_image = QImage("./assets/icons/cross.png")
        background = QPixmap(del_image)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(background))
        self.del_button.setPalette(palette)
