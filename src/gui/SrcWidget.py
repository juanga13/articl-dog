"""
Sources Widget

@description: menu for Main window, has a editable
              list of all sources.
"""


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class SrcWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("src")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from EDIT SOURCES")

        layout.addWidget(test_label)

        self.setLayout(layout)
