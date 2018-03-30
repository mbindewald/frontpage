from flask import Flask, jsonify
app = Flask(__name__)

# todo: secure with auth0? So that only the right website can access api

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

# todo: Example trend data, will eventually be replaced with a function that grabs
# the information from the database
def getTrends():
    trends = {
        'timestamp': '12/31/2018',
        'trends': [
            {
            'trendName': 'firstExample',
            'tweetCount': 100,
            'tweetEmbedLink': 'xxxx.com',
            'googleNewsEmbedLink': 'xxxx.com',
            'youtubeEmbedLink': 'xxxx.com'
            },
            {
            'trendName': 'secondExample',
            'tweetCount': 100,
            'tweetEmbedLink': 'xxxx.com',
            'googleNewsEmbedLink': 'xxxx.com',
            'youtubeEmbedLink': 'xxxx.com'
            }
        ]
    }

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