// ./app.js

const vm = new Vue({
  el: '#app',
  data: {
    results: []
  },
  mounted() {
    axios.get('http://ec2-54-84-86-55.compute-1.amazonaws.com:5000/api').then(response => {
      this.results = response.data.results
    })
  }
});
