from flask import Flask, request, make_response, json
import boto3
from botocore.exceptions import ClientError
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

# TODO: secure with auth0? So that only the right website can access api
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('InformationDB')

def getTrends():
    try:
        response = table.query(
            KeyConditionExpression='filler = :fill',
            ExpressionAttributeValues= {
                ':fill': 'fill'
            },
            ScanIndexForward=False,
            Limit=1
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return 'server error'
    else:
        items = response['Items'][0]
        del items['filler'] # remove unnecessary primary key
        return items

# encode trend html elements in base64 so that we can inject them in Vue
def encodeTrendHtml(items):
    completeTrends = []

    # guarantee that we're only displaying trends with all data
    for trend in items['trends']:
        if len(trend['twitter_post']) == 1 and len(trend['youtube_post']) == 1:
            completeTrends.append(trend)

    for trend in completeTrends:
        trend['twitter_post'][0]['html'] = base64.b64encode(bytes(trend['twitter_post'][0]['html'], "utf-8"))
        trend['youtube_post'][0] = base64.b64encode(bytes(trend['youtube_post'][0], "utf-8"))

    items['trends'] = completeTrends

    return items

@app.route("/")
def main():
    # TODO: Have this route be an informational page so that people hitting our
    # server will know what it is/have instructions to use it

    information = "This API is used for our CS495 project found here:"
    return information


@app.route("/api")
def api():
    resp = make_response(json.dumps(encodeTrendHtml(getTrends())))
    resp.headers['content-type'] = 'application/json'
    return(resp)