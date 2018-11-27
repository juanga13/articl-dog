import newspaper

if __name__ == '__main__':
    cancilleria_gov = newspaper.build("https://www.cancilleria.gob.ar/es/actualidad/noticias/")
    # campana_noticias = newspaper.build("http://www.campananoticias.com/")
    # cnn_news = newspaper.build("http://cnn.com")
    # cancilleria_gov.download()
    # cancilleria_gov.parse()
    print(cancilleria_gov.articles)
    # print(cancilleria_gov.html)
    for article in cancilleria_gov.articles:
        print(article.url)
