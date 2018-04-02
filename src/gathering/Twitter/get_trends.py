#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------
import tweepy
from twitter import *
import boto3

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_key"], config["access_secret"])

api = tweepy.API(auth)

#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
results = twitter.trends.place(_id = 23424977)

print "US Trends"
# print results

for location in results:
    i = 0
    for trend in location["trends"]:
        print " - %s" % trend["name"]
        popular_tweets = api.search(q=trend["name"], result_type='popular')
        print popular_tweets
        print "\n"
        i+=1

print i
