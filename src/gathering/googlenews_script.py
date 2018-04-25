import json
from newsapi import NewsApiClient

def get_top_article(data):

    top_article = {}
    if data and data['articles']:
        top_article['title'] = data['articles'][0]['title']
        top_article['description'] = data['articles'][0]['description']
        top_article['url'] = data['articles'][0]['url']
        top_article['urlToImage'] = data['articles'][0]['urlToImage']

    return top_article

def googlenews_search(trend):

    api = NewsApiClient(api_key='386530c989c5478888d26532466fdf30')
    data = api.get_top_headlines(q=trend, country='us', language='en')
    top_article = get_top_article(data)

    return top_article

def main():
    googlenews_search('bitcoin')

if __name__ == "__main__":
    main()
