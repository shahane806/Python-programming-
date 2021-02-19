import requests
import json


def news():
    """
    news
    """
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=fa2fcf7961c04df3ad8e42903935afa2"
    news = requests.get(url).text
    news_py = json.loads(news)
    art = news_py['articles']
    for articles in art:
        print(articles['title'])


if __name__ == '__main__':
    news()
