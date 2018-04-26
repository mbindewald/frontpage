<!DOCTYPE html>
<html lang="en">
<!-- tweet_volume -->

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">

    <title>FrontPage</title>

    <!-- Required Stylesheets -->
    <link type="text/css" rel="stylesheet" href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css" />

    <!-- Required scripts -->
    <script src="https://unpkg.com/vue"></script>
    <script src="https://unpkg.com/babel-polyfill@latest/dist/polyfill.min.js"></script>
    <script src="https://unpkg.com/bootstrap-vue@latest/dist/bootstrap-vue.js"></script>
    <script import TweetEmbed from 'react-tweet-embed'> </script>
    <style>
        body {
            font-family: "Helvetica";
            font-size: 18px;
        }

        .jumbotron {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        }

        .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            background-size: contain;
            height: 100%;
        }

        .tweet-card {
            padding: 5px;
        }

        .tweet-image {
            max-height: 100px;
            max-width: 100px;
            margin: auto;
        }

        .card-image {
            background-size: contain;
            background-position: center top;
            background-repeat: no-repeat;
            width: 100%;
            height: auto;
            height: auto;
            overflow: hidden;
            display: block;
        }


        .card-title {
            font-size: 20px;
            left: 0;
            right: 0;
            padding: 16px 4px 0 4px;
            font-weight: 400;
            white-space: nowrap;
            text-overflow: ellipsis;
            font-weight: bold;
            overflow: hidden;
            border-bottom: 1px solid;
        }

        .card-subtitle {
            font-size: 18px;
            padding: 4px;
            margin: 0;
            line-height: 1.6;
            color: #000;
            overflow: hidden;
        }

        .card-action-bar {
            position: absolute;
            bottom: 0;
            top: auto;
            left: 0;
            right: 0;
            padding: 0 8px;
            boz-sizing: border-box;
            height: 52px;
        }

        .card-button {
            outline: none;
            position: relative;
            display: inline-block;
            line-height: 1.6;
            padding: 0 16px;
            cursor: pointer;
        }

        .grid-container {
            width: 100%;
            height: 100%;
            display: grid;
            grid-gap: 10px;
            padding: 10px;
        }

        .grid-item {
            background-color: rgba(255, 255, 255, 0.8);
            text-align: center;
            padding: 20px;
            font-size: 10px;
        }

        .item1 {
            grid-column: 1;
            grid-row: 1;
        }

        .item2 {
            grid-column: 2 / 4;
            grid-row: 1 / 4;
        }

        .item3 {
            grid-column: 1 / 2;
            grid-row: 2 / 4;
        }

        .item4 {
            grid-column: 1 / 4;
            grid-row: 5;
        }

        .thumbnail img {
            height: 100%;
            width: auto;
        }

        .story-panel {
            margin-left: 0px;
            margin-right: 0px;
            margin-bottom: 30px;
        }

        .video-container {
            position: relative;
            padding-bottom: 27%;
            padding-top: 35px;
            height: 0;
            overflow: hidden;
        }

        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .search-bar {
            display: inline-block;
            margin-bottom: 8px;
            width: 100%;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
            background-color: #e9ecef;
            padding: 8px;
        }

        .search-button {
            height: 100%;
            text-align: center;
            vertical-align: middle;
            display: flex;
            align-items: flex-end;
        }

        .search-input {
            width: 25%;
            float: right;
            vertical-align: center;
        }

        .search-box {
            padding: 0 0 0 4px;
        }
    </style>
</head>

<body>
  <div id="app" class="search-bar">
      <div class="search-input">
          <form action ="index.php" method="get">
              <div class="input-group">
                  <input name="userInput" type="text" id="userInput" class="form-control search-box" placeholder="Search">
                  <button class="btn btn-primary btn-sm search-button" type="submit">Submit</button>
                  <!-- <a id"searchButtonOut" href="#" target="_self" class="btn btn-primary btn-sm search-button" role="button" type="submit">Go</a> -->
              </div>
          </form>
      </div>
  </div>


    <div class="container-fluid" id="render">
        <div class="jumbotron">
            <h1 class="display-4">FrontPage</h1>
            <p class="lead">The Internet's News In One Place</p>
            <p>For more information visit our website</p>
            <p class="lead">
                <a class="btn btn-primary btn-lg" href="https://mbindewald.github.io/frontpage/" role="button">Learn more</a>
            </p>
        </div>

        <div class="card card-primary story-panel" v-for="(trend, index) in results.trends" v-if="trend.trend === <?php echo $_GET["userInput"]; ?>">
            <div class="card-header">
                {{ trend.trend }}
            </div>
            <div class="card-body">
                <div class="row" v-if="trend.googlenews_post.url !== 'none'">
                    <div class="col-md-4" v-for="tweet in trend.twitter_post">
                        <div class="card tweet-card">
                            <img class="card-img-top tweet-image" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/281152/Twitter_bird_logo_2012.svg">
                            <span class="card-body" v-html="myFunctionTweet(tweet)"></span>
                        </div>
                    </div>
                    <div class="col-md-4 video-container" v-html="myFunctionYoutube(trend.youtube_post)"></div>

                    <div class="col-md-4">
                        <a :href="trend.googlenews_post.url">
                            <div class="card">
                                <img class="card-image" :src="trend.googlenews_post.urlToImage">
                                <h2 class="card-title">{{ trend.googlenews_post.title }}</h2>
                                <p class="card-subtitle">{{ trend.googlenews_post.description }}</p>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="row" v-if="trend.googlenews_post.url == 'none'">
                    <div class="col-md-6" v-for="tweet in trend.twitter_post">
                        <div class="card tweet-card">
                            <img class="card-img-top tweet-image" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/281152/Twitter_bird_logo_2012.svg">
                            <span class="card-body" v-html="myFunctionTweet(tweet)"></span>
                        </div>
                    </div>
                    <div class="col-md-6 video-container" v-html="myFunctionYoutube(trend.youtube_post)"></div>
                </div>
            </div>
        </div>


    </div>
    <script src="https://unpkg.com/vue"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue-resource@1.5.0"></script>
    <script src="render.js"></script>
</body>

</html>
