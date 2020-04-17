<template>
  <div>
    <h1>Test Analytics</h1>
    <h2>Your Recent Tests</h2>
    <canvas id="myChart" width="1100" height="500"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js';

  export default {
    name: 'Analytics',
    mounted() {
      var config = {
        type: 'line',
        data: {
          labels: ['SAT #1', 'SAT #2', 'SAT #3', 'SAT #4', 'SAT #2', 'SAT #1', 'SAT #3'],
          datasets: [{
            label: 'Reading',
            backgroundColor: '#f36b57',
            borderColor: '#f36b57',
            data: [
              68,
              75,
              73,
              80,
              82,
              83,
              87
            ],
            fill: false,
          }, {
            label: 'Writing',
            fill: false,
            backgroundColor: '#f7931e',
            borderColor: '#f7931e',
            data: [
              65,
              70,
              77,
              74,
              80,
              83,
              84
            ],
          }, {
            label: 'Math',
            fill: false,
            backgroundColor: '#8cc63f',
            borderColor: '#8cc63f',
            data: [
              79,
              76,
              80,
              82,
              84,
              83,
              85
            ],
          }, {
            label: 'Math (Calculator)',
            fill: false,
            backgroundColor: '#c1272d',
            borderColor: '#c1272d',
            data: [
              85,
              88,
              86,
              90,
              88,
              91,
              94
            ],
          }]
        },
        options: {
          responsive: true,
          title: {
            display: true,
            text: 'Your Recent Test Scores'
          },
          tooltips: {
            mode: 'index',
            intersect: false,
          },
          hover: {
            mode: 'nearest',
            intersect: true
          },
          scales: {
            xAxes: [{
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Tests Taken'
              }
            }],
            yAxes: [{
              display: true,
              scaleLabel: {
                display: true,
                labelString: 'Score (%)'
              }
            }]
          }
        }
      };
      var ctx = document.getElementById('myChart').getContext('2d');
			window.myLine = new Chart(ctx, config);
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1 {
    font-size: 3rem;
    margin-top: 2rem;
  }

  #myChart {
    letter-spacing: 0;
    max-width: 90%;
    margin-right: 50px;
  }
</style>
