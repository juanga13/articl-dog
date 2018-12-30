"""==============================================
Animated button

@description: changes image when idle, pressed
              and hovered
=============================================="""


from PyQt5.QtGui import QPainter, QPixmap

from PyQt5.QtWidgets import QPushButton


class AnimatedButton(QPushButton):

    def __init__(self, resources):
        super().__init__()

        """resources = ["url/to/idle/image",
                        "url/to/pressed/image",
                        "url/to/hover/image"]"""
        self.pixmap = QPixmap(resources[0])
        self.pixmap_pressed = QPixmap(resources[1])
        self.pixmap_hover = QPixmap(resources[2])

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)
