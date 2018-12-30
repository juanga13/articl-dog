"""

"""

import os

import shutil

# TODO finish some method


class TmpDataController:
    file = None
    line_cursor = 0
    first_time_bool = None

    def __init__(self):
        print("init tmp")
        if not os.path.exists("./tmp"):
            os.makedirs("./tmp")

        # comment writings
        comments = ["# ====================================================\n",
                    "# This space is reserved for a clean documentation.\n",
                    "# \n",
                    "# data.jdt saves all instance data of the program\n",
                    "# inside, like temporary settings and articles loaded,\n",
                    "# so that the program does not asks to internet again\n",
                    "# all the data.\n",
                    "# \n",
                    "# name=TempraryDataController/ver=0.1/author=juanga13\n",
                    "#\n",
                    "# multiple-url-separator='|'\n",
                    "# ====================================================\n"]
        with open("./tmp/data.jdt", "w") as file:
            file.writelines(comments)
            self.line_cursor += 12

        print("file object:" + str(self.file.__str__()))

        print("y no write test boi")

    def write_article(self, article, first_time_bool):
        """:param article: title, summary, text, publish_date, image_urls"""
        article_data = [article.title + "\n",
                        article.summary + "\n",
                        article.text + "\n",
                        str(article.images) + "\n",
                        article.publish_date + "\n"]
        with open("./tmp/data.jdt", "a") as file:
            file.seek(self.line_cursor)
            file.writelines(article_data)

        if first_time_bool is True:
            self.first_time_bool = True
        else:
            self.first_time_bool = False

    def get_all_articles(self):
        pass

    def __del__(self):
        print(str(self.__str__()) + " is being destroyed, closing temporary data")
        shutil.rmtree("./tmp")
