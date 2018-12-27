import newspaper


# ==============================================
# gets all articles given a source link (string)
#
# @returns a list of Article object
# ==============================================
def get_article_data(sources):
    # check sources
    if sources is None:
        return []
    # check temporary data
    # TODO if temp data exists, do not fetch from internet

    # TODO get every article from every source and save to temp
    print("getting articles from source (" + sources + ")")

    result = []
    builds = []
    for url in sources:
        build = newspaper.build(sources, memoize_articles=False)
        for article in build.articles:

            # filter some articles that are not articles
            # for some reason
            if str(article.url).startswith(sources):
                article.download()
                article.parse()
                print("title=" + str(article.title))
                result.append(article)

    return result
