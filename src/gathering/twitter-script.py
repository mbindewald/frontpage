#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *


def twitter_search(key):
    #-----------------------------------------------------------------------
    # load our API credentials
    #-----------------------------------------------------------------------
    config = {}
    execfile("config.py", config)

    #-----------------------------------------------------------------------
    # create twitter API object
    #-----------------------------------------------------------------------
    twitter = Twitter(
    		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


    #-----------------------------------------------------------------------
    # perform a basic search
    # Twitter API docs:
    # https://dev.twitter.com/rest/reference/get/search/tweets
    #-----------------------------------------------------------------------
    query = twitter.search.tweets(q = key, result_type = "popular", count = "1")

    #-----------------------------------------------------------------------
    # How long did this query take?
    #-----------------------------------------------------------------------
    print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

    # api = twitter.Api(consumer_key = config["consumer_key"],
    #                   consumer_secret = config["consumer_secret"],
    #                   access_token_key = config["access_key"],
    #                   access_token_secret = config["access_secret"])
    # #-----------------------------------------------------------------------
    # # Loop through each of the results, and print its content.
    # #-----------------------------------------------------------------------
    for result in query["statuses"]:
    	print "(%s) @%s %s %s" % (result["created_at"], result["user"]["screen_name"], result["text"], result["entities"]["urls"][0]["url"])
    #     # link = twitter.GetStatusOembed(url=result["entities"]["urls"][0]["display_url"])
    #     link = api.GetStatusOembed(status_id=result["id"],url=result["entities"]["urls"][0]["display_url"])

        # print "%s" % link


# try:
#     twitter_search()
# except HttpError, e:
#     print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
