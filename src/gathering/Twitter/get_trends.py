#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------
import tweepy
from twitter import *
import boto3
import datetime
from config import consumer_secret, consumer_key, access_key, access_secret

def lambda_handler(event, context):
    #-----------------------------------------------------------------------
    # Get current time
    #-----------------------------------------------------------------------
    curTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');

    #-----------------------------------------------------------------------
    # create twitter API object
    #-----------------------------------------------------------------------
    twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

    #-----------------------------------------------------------------------
    # retrieve global trends.
    # other localised trends can be specified by looking up WOE IDs:
    #   http://developer.yahoo.com/geo/geoplanet/
    # twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
    #-----------------------------------------------------------------------
    results = twitter.trends.place(_id = 23424977)
    client = boto3.client("dynamodb")

    trends = []
    for location in results:
        for trend in location["trends"]:
            #popular_tweets = api.search(q=trend["name"], result_type='popular')
            trends.append(trend["name"])

    response = client.put_item(
        TableName='TrendDB',
        Item={
            'filler': {
                'S': 'trend'
            },
            'time': {
                'S': curTime
            },
            'trends': {
                'SS': trends
            }
        }
    )

    return response
