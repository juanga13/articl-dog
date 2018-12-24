from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

""" =============================================
Article Widgets
@description : has the card widgets, depending on
               the align you want (Grid, List, 
               etc.)    
=============================================="""
# TODO finish ArticleListCard


# ===============================================
# Article Grid Card
# ===============================================
class ArticleGridCard(QWidget):

    # -------------------------------------------
    # Init
    # -------------------------------------------
    def __init__(self, q_size, photo_path,
                 title, description, date):
        super().__init__()
        self.photo_path = photo_path
        self.title = title
        self.description = description
        self.date = date

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

        self.setStyleSheet("background-image: url("
                           + self.photo_path)

        self.setLayout(layout)


# ===============================================
# Article List Card
# ===============================================
class ArticleListCard(QWidget):

    def __init__(self, q_size, photo,
                 title, description, date):
        super().__init__()
        self.photo = photo
        self.title = title
        self.description = description
        self.date = date

        self.init_ui(q_size)

    def init_ui(self, q_size):
        # layout =
        pass
