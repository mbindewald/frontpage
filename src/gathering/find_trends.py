# shouldn't need this later, just for testing
import sys
import json
import datetime
import boto3
from boto3.dynamodb.conditions import Key, Attr
from youtube_script import youtube_search
from twitter_script import twitter_search
from googlenews_script import googlenews_search


dynamodb = boto3.resource("dynamodb")
trend_table = dynamodb.Table("TrendDB")
info_table = dynamodb.Table("InformationDB")
cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
prev_time = str(datetime.datetime.now() - datetime.timedelta(minutes=15))

def get_trends():

    items = []
    response = trend_table.scan(
        FilterExpression=Attr('time').between(prev_time, cur_time)
    )
    items.append(response['Items'])
    while 'LastEvaluatedKey' in response:
        response = trend_table.scan(
            FilterExpression=Attr('time').between(prev_time, cur_time),
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items.append(response['Items'])

    return response['Items']

def put_trend_in_dynamodb(trend_objs):

    response = info_table.put_item(
        Item={
            'filler': 'fill',
            'time': cur_time,
            'trends': trend_objs
        }
    )
    print(trend_objs)

    return response

def parse_trends(trends_obj):

    trends_arr = []
    for trend in trends_obj['trends']:
        pair = []
        pair.append(trend['name'])
        pair.append(trend['tweet_volume'])
        trends_arr.append(pair)

    return trends_arr

def find_all_trends(trends):

    trend_objs = []
    for trend in trends:
        twitter_trend = twitter_search(trend[0])
        youtube_trend = youtube_search(trend[0])
        #googlenews_trend = googlenews_search(trend[0])
        trend_obj = {}
        trend_obj["trend"] = trend[0]
        trend_obj["tweet_volume"] = trend[1]
        trend_obj["youtube_post"] = youtube_trend
        trend_obj["twitter_post"] = twitter_trend
        # if googlenews_trend is not "":
        #     trend_obj["googlenews_post"] = googlenews_trend
        trend_objs.append(trend_obj)
    print(trend_objs)
    return put_trend_in_dynamodb(trend_objs)


def lambda_handler(event, context):

    trends_obj = get_trends()
    trends = parse_trends(trends_obj[0])
    response = find_all_trends(trends)

    return response
