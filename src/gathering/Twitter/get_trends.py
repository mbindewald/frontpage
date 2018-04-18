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
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TrendDB')
    trends = []
    for location in results:
        for trend in location["trends"]:
            trends.append(trend)

    response = table.put_item(
        Item={
            'filler': 'trend',
            'time': curTime,
            'trends': trends
        }
    )

    return response
