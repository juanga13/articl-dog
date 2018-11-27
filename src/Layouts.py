from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton


class Layouts:

    def __init__(self):

        self.layout_dict = {
            "Top Bar": self.generate_top_bar(),
            "Main Hub": self.generate_main_hub()
            # "Options Menu": self.generate_options_menu()
        }

    def generate_top_bar(self):

        layout = QHBoxLayout()

        main_hub_button = QPushButton()
        main_hub_button.setFixedSize(100, 100)

    # ======================
    # Main Hub Layout
    # ======================

    def generate_main_hub(self):

        layout = QVBoxLayout()



    # def generate_options_menu(self):
    #
    #     pass