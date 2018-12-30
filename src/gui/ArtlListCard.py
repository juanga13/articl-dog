from PyQt5.QtWidgets import QWidget

# TODO finish this


class ArteListCard(QWidget):
    """

    """

    def __init__(self, q_size, photo, title, description, date, photo_path):
        super().__init__(photo_path, title, description, date)
        self.photo = photo
        self.title = title
        self.description = description
        self.date = date

        self.init_ui(q_size)

    def init_ui(self, q_size):
        # layout =
        pass
