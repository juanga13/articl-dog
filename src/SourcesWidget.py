"""

"""

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QHBoxLayout,\
    QLineEdit, QApplication, QMainWindow

from AnimatedButton import AnimatedButton


class EditSourceWidget(QWidget):
    """==============================================
    Edit source widget

    @description widget for the source list in edit
    source menu.
    =============================================="""
    def __init__(self, url):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)

        # self: action manage from Controller
        self.url_edit = QLineEdit(url)
        self.url_edit.adjustSize()

        # ----------------------------------------------- test BEGIN
        button_resources_test = ["./assets/icons/cross.png",
                                 "./assets/icons/app.png",
                                 "./assets/icons/edit.png"]
        self.del_button = AnimatedButton(button_resources_test)
        # ----------------------------------------------- test END
        # TODO [IMAGE] set delete button idle, hover and pressed images

        self.del_button.setFixedWidth(self.url_edit.height())

        layout.addWidget(self.url_edit)
        layout.addWidget(self.del_button)

        self.setLayout(layout)
