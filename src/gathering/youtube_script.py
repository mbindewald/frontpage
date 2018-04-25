#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python geolocation_search.py --q=surfing --location-"37.42307,-122.08427" --location-radius=50km --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyBPSqRwDCiZn04T6kCcplzEIZq238jKpnk'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(key):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)


    # Call the search.list method to retrieve vides with keyword by viewcount.
    search_response = youtube.search().list(
        # id=video_ids,
        # chart='mostPopular',
        type = 'video',
        regionCode='us',
        part='snippet, id',
        videoEmbeddable = 'true',
        order = 'viewCount',
        q = key,
        maxResults = 1
    ).execute()

    search_videos = []

    global video_ids

    # Merge video ids
    for search_result in search_response.get('items', []):
        search_videos.append(search_result['id']['videoId'])
        video_ids = ','.join(search_videos)

    # Call the videos.list method to retrieve player details for each video.
    video_response = youtube.videos().list(
        id=video_ids,
        part='snippet, player'
        ).execute()

    videos = []

    # Add each result to the list, and then display the list of matching videos.
    for video_result in video_response.get('items', []):
        videos.append('%s' % (video_result['player']['embedHtml']))
        # videos.append('%s, %s' % (video_result['snippet']['title'],
        #                               video_result['player']['embedHtml']))

    # print 'YOUTUBE HTML\n', '\n'.join(videos), '\n'
    # obviously this is only going to return the most recent my_html, but since we are only pulling 1 video at a time it doesn't matter
    return videos
