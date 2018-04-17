#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import sys


def twitter_search(key):
    #-----------------------------------------------------------------------
    # load our API credentials
    #-----------------------------------------------------------------------
    config = {}
    execfile("config.py", config)

    #-----------------------------------------------------------------------
    # create twitter API object
    #-----------------------------------------------------------------------

    global twitter

    twitter = Twitter(
    		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))



    #-----------------------------------------------------------------------
    # perform a basic search
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    query = twitter.search.tweets(q = key, result_type = "popular", count = "1")


    for result in query["statuses"]:
        my_html = twitter.statuses.oembed(_id=result["id"])
        print "TWEET HTML"
        print "%s" % (my_html["html"])
