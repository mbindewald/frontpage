from newsapi import NewsApiClient


api = NewsApiClient(api_key='386530c989c5478888d26532466fdf30')

api.get_top_headlines(sources='bbc-news')

print(api.get_top_headlines(country='us'))
