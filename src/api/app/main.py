from flask import Flask, jsonify
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

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
        print(items)
        return items


@app.route("/")
def main():
    # TODO: Have this route be an informational page so that people hitting our
    # server will know what it is/have instructions to use it

    information = "This API is used for our CS495 project found here:"
    return information


@app.route("/api")
def api():
    # TODO: memcache or similar for caching?

    return jsonify(getTrends())
