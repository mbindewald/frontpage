// ./app.js

new Vue({
  el: '#app',
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
      console.log("success")
    }, response => {
      // error callback
      console.log(JSON.stringify(response))
    });
  }
})

/*
const vm = new Vue({
  el: '#app',
  data: {
    info: []
  },
  mounted() {
    axios.get('http://ec2-54-84-86-55.compute-1.amazonaws.com:5000/api').then(response => {
      this.info = response.data
    }, response => {
      // error callback
      console.log(JSON.stringify(response))
    });
  }

});
*/
