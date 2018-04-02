# #-----------------------------------------------------------------------
# # Justin Lukas
# # Programming Assignment 2
# # CS 491 with Dr. Aibek Musaev
# # Due date: 9/24/2017
# #-----------------------------------------------------------------------
# from twitter import *
#
# import collections
# from collections import Counter
# import time
# import datetime
# import io
#
# try:
#     import json
# except ImportError:
#     import simplejson as json
#
# # set up file to write report to
# f = io.open('results.txt', 'w', encoding = "utf-8")
#
# # make this end
# start = datetime.datetime.now()
# start_string = "<%s>\t" % start
# start_string = start_string.decode('utf-8')
# f.write(start_string)
#
# config = {}
# execfile("config.py", config)
#
# auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
# stream = TwitterStream(auth = auth, secure = True, _id = 23424977)
#
# startTime = time.time()
# PERIOD_OF_TIME = 60 * 1
#
# hashtags = []
#
# tweet_iter = stream.statuses.sample()
#
# for tweet in tweet_iter:
#     if time.time() > startTime + PERIOD_OF_TIME : break
#     if 'text' in tweet:
#         for hashtag in tweet['entities']['hashtags']:
#         	hashtags.append(hashtag['text'].lower())
#
# # make this start?
# end = datetime.datetime.now()
# end_string = "<%s>\n" % end
# end_string = end_string.decode('utf-8')
# f.write(end_string)
#
# topten = Counter(hashtags).most_common(50)
# for i in topten:
#    f.write("<%s>\t<%s>\n" % (i[0], i[1]))
#
#

#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------
import tweepy
from twitter import *

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
