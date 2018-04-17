import json
from newsapi import NewsApiClient


api = NewsApiClient(api_key='386530c989c5478888d26532466fdf30')

# print(api.get_top_headlines(q='specific headline', country='us', page_size=1))

with open('data.json', 'w') as outfile:
    json.dump(api.get_top_headlines(country='us', page_size=1), outfile)

data = api.get_top_headlines(country='us', page_size=1)
print data['articles'][0]['url']
