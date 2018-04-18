# shouldn't need this later, just for testing
import sys
import json

execfile("youtube-script.py")
execfile("twitter-script.py")

trends = ["trump", "tiger  woods"]

def find_all_trends(trends):

    for trend in trends:
        twitter_trend = twitter_search(trend)
        youtube_trend = youtube_search(trend)
        # googlenews_trend = googlenews_search(trend)
        trend_obj = {}
        trend_obj["trend"] = trend
        trend_obj["youtube_post"] = youtube_trend
        trend_obj["twitter_post"] = twitter_trend
        # trend_obj["googlenews_post"] = googlenews_trend
        json_data = json.dumps(trend_obj)
        print "%s TREND DATA : \n %s" % (trend_obj["trend"], json_data)

try:
    find_all_trends(trends)
except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
