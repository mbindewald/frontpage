from flask import Flask, jsonify
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# todo: secure with auth0? So that only the right website can access api

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

# todo: Example trend data, will eventually be replaced with a function that grabs
# the information from the database

client = boto3.client('dynamodb')


def getTrends():
    try:
        response = client.query(
            TableName='InformationDB',
            IndexName='fill',
        )


    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']

    '''
    trends =
        {
            "filler": "fill",
            "time": "2008-03-09 16:05:07.123",
            "trends": [
                {
                    "googleNewsEmbedLink": "xxxx.com",
                    "trendName": "firstExample",
                    "tweetCount": 100,
                    "tweetEmbedLink": "xxxx.com",
                    "youtubeEmbedLink": "xxxx.com"
                },
                {
                    "googleNewsEmbedLink": "xxxx.com",
                    "trendName": "secondExample",
                    "tweetCount": 90,
                    "tweetEmbedLink": "xxxx.com",
                    "youtubeEmbedLink": "xxxx.com"
                },
                {
                    "googleNewsEmbedLink": "xxxx.com",
                    "trendName": "thirdExample",
                    "tweetCount": 90,
                    "tweetEmbedLink": "xxxx.com",
                    "youtubeEmbedLink": "xxxx.com"
                }
            ]
        }
        '''

    return trends


@app.route("/")
def main():
    # Have this route be an informational page so that people hitting our
    # server externally will know what it is.

    information = "This API is used for our CS495 project found here:"
    return information


@app.route("/api")
def api():
    # memcache eventually for caching?

    return jsonify(getTrends())
