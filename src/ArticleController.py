import newspaper


# ==============================================
# gets all articles given a source link (string)
#
# @returns a list of Article object
# ==============================================
def get_article_from_source(source):
    if source is None:
        return []

    # demo
    source = "https://www.cancilleria.gob.ar/es/actualidad/noticias"

    result = []

    build = newspaper.build(source, memorize_articles=False)
    for article in build.articles:
        if str(article.url).startswith(source):
            result.append(article)

    # for article in result:
        # print(article.url)

    return result
