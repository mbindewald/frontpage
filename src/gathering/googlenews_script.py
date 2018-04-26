import json
from newsapi import NewsApiClient

def get_top_article(data):

    top_article = {}
    if not data['articles']:
        top_article['title'] = 'none'
        top_article['description'] = 'none'
        top_article['url'] = 'none'
        top_article['urlToImage'] = 'none'
    else:
        top_article['title'] = data['articles'][0]['title']
        top_article['description'] = data['articles'][0]['description']
        top_article['url'] = data['articles'][0]['url']
        top_article['urlToImage'] = data['articles'][0]['urlToImage']

    return top_article

def googlenews_search(trend):

    api = NewsApiClient(api_key='2adf8850e325465786cc2af0e8d6fb33')
    data = api.get_top_headlines(q=trend, country='us', language='en')
    top_article = get_top_article(data)

    return top_article

def main():
    data = googlenews_search('bitcoin')
    if not data:
        print("empty")
    else:
        print(data)

if __name__ == "__main__":
    main()
