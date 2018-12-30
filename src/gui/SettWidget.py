from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class SettWidget(QWidget):
    """===============================================
    Settings Widget

    @description: menu for main window.
    =============================================="""

    def __init__(self):
        super().__init__()
        self.setObjectName("sett")
        layout = QVBoxLayout()

        test_label = QLabel("This is a test from SETTINGS")

        layout.addWidget(test_label)

        self.setLayout(layout)
