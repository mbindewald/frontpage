# shouldn't need this later, just for testing
import sys

execfile("youtube-script.py")
execfile("twitter-script.py")

trends = ["trump", "tiger  woods"]

def find_all_trends(trends):
    for trend in trends:
        twitter_search(trend);
        youtube_search(trend);


try:
    find_all_trends(trends)
except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
