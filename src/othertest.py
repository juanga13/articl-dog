import newspaper


def run1():
    c = newspaper.build('https://www.cbs.com/')
    for article in c.articles:
        print(article.url)


def run2():
    c = newspaper.build('https://www.cancilleria.gob.ar/es/actualidad/noticias', memoize_articles=False)
    for article in c.articles:
        print(article.url)


if __name__ == '__main__':
    run2()
