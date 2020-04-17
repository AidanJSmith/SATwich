<template>
  <div>
    <h1>Dashboard</h1>
    <h2>Your Progress</h2>
    <section class="flex">
      <section id="progress-cards" class="flex-wrap">
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_bread.svg" alt="Bread" />
            <h3>Speed</h3>
          </div>
          <p>Your average speed is <b>1</b> question every <b>{{speed}}</b> minutes. This is <b>average</b>!</p>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_cheese.svg" alt="Cheese" />
            <h3>Accuracy</h3>
          </div>
          <p>On average, you miss <b>{{Math.round((read_correct+write_correct+calc_correct+nocalc_correct)/(read_total+write_total+calc_total+nocalc_total)*100) }}</b> out of every <b>100</b> questions. This is <b>average</b>!</p>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_bacon.svg" alt="Bacon" />
            <h3>Reading</h3>
          </div>
          <p>Your score for reading is <b>{{Math.round(read_correct*100/read_total)}}%</b> or <b>{{read_correct}}/{{read_total}}</b> questions answered correctly. This is <b>good</b>!</p>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_tomato.svg" alt="Tomato" />
            <h3>Writing</h3>
          </div>
          <p>Your score for writing is <b>{{Math.round(write_correct*100/write_total)}}%</b> or <b>{{write_correct}}/{{write_total}}</b> questions answered correctly. This is <b>good</b>!</p>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_leaf.svg" alt="Greens" />
            <h3>Math</h3>
          </div>
          <p>Your score for math is <b>{{Math.round(nocalc_correct*100/nocalc_total)}}%</b> or <b>{{nocalc_correct}}/{{nocalc_total}}</b> questions answered correctly. This is <b>good</b>!</p>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd_bread.svg" alt="Bread" />
            <h3>Math <span class="oi" data-glyph="calculator" title="Calculator" aria-hidden="true"></span></h3>
          </div>
          <p>Your score for math is <b>{{Math.round(calc_correct*100/calc_total)}}%</b> or <b>{{calc_correct}}/{{calc_total}}</b> questions answered correctly. This is <b>good</b>!</p>
        </div>
      </section>
    </section>
    <h2>Your Recommendations</h2>
  </div>
</template>

<script>
import json from "../data/data.json"

export default {
  name: 'Dashboard',
  data: function () {
    return{
          speed:0,
          read_correct:0,
          read_total:0,
          write_correct:0,
          write_total:0,
          calc_correct:0,
          calc_total:0,
          nocalc_correct:0,
          nocalc_total:0,
      }
  },
  mounted() {
    let parsed=JSON.parse(json);
    this.speed=parsed["speed"]
    this.read_correct=parsed["reading"]["correct"]
    this.read_total=parsed["reading"]["total"]
    this.write_correct=parsed["writing"]["correct"]
    this.write_total=parsed["writing"]["total"]
    this.calc_correct=parsed["calc"]["correct"]
    this.calc_total=parsed["calc"]["total"]
    this.nocalc_correct=parsed["nocalc"]["correct"]
    this.nocalc_total=parsed["nocalc"]["total"]
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1 {
    font-size: 3rem;
    margin-top: 2rem;
  }

  .flex {
    display: flex;
    padding-right: 50px;
  }

  .card {
    width: 250px;
  }
</style>
