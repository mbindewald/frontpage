#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import sys
from config import consumer_secret, consumer_key, access_key, access_secret

def twitter_search(key):
    #-----------------------------------------------------------------------
    # create twitter API object
    #-----------------------------------------------------------------------
    global twitter
    twitter = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

    #-----------------------------------------------------------------------
    # perform a basic search
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    query = twitter.search.tweets(q = key, result_type = "popular", count = "1")

    my_html = []
    for result in query["statuses"]:
        my_html.append(twitter.statuses.oembed(_id=result["id"]))
        # print "TWEET HTML"
        # print "%s" % (my_html["html"])

    # obviously this is only going to return the most recent my_html, but since we are only pulling 1 tweet at a time it doesn't matter
    return my_html
