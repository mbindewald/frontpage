// ./render.js

function b64DecodeUnicode(str) {
  return decodeURIComponent(Array.prototype.map.call(atob(str), function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
  }).join(''))
}

function searchKeyword() {
  console.log(document.getElementById("userInput").value)
  var element = document.getElementById("searchButtonOut")
  element = document.getElementById("userInput").value
  // document.getElementById('displayWindow').v-if='trend.trend === 'document.getElementById('app').value''
}

new Vue({
  el: '#render',
  data () {
    return {
      results: null
    }
  },
  mounted () {
    // GET /someUrl
    this.$http.get('http://ec2-54-84-86-55.compute-1.amazonaws.com:5000/api').then(response => {
      // success callback
      this.results = response.body
      // this.results = atob(response.body)
      console.log("success")

      this.results.trends.sort(function(a, b){
          if(a.tweet_volume > b.tweet_volume) return -1;
          if(a.tweet_volume < b.tweet_volume) return 1;
          return 0;
      })

    }, response => {
      // error callback
      console.log("error")
    });
  },
  methods:{
    myFunctionTweet: function (tweet) {
        return b64DecodeUnicode(tweet.html)
		    // this.html = atob(this.html)
    },

    myFunctionYoutube: function (youtube) {
        return b64DecodeUnicode(youtube)
    }

  }
});
