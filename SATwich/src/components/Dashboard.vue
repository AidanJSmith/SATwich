<template>
  <div>
    <h1>Dashboard</h1>
    <h2>Your Progress</h2>
    <section class="progress">
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_bread.svg" />
          <h3>Speed</h3>
        </div>
        <p>Your average speed is <b>1</b> question every <b>3.2</b> minutes. This is <b>average</b>!</p>
      </div>
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_cheese.svg" />
          <h3>Accuracy</h3>
        </div>
        <p>On average, you miss <b>1</b> out of every <b>9</b> questions. This is <b>average</b>!</p>
      </div>
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_bacon.svg" />
          <h3>Reading</h3>
        </div>
        <p>Your score for reading is <b>90%</b> or <b>90/100</b> questions answered correctly. This is <b>good</b>!</p>
      </div>
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_tomato.svg" />
          <h3>Writing</h3>
        </div>
        <p>Your score for writing is <b>95%</b> or <b>95/100</b> questions answered correctly. This is <b>great</b>!</p>
      </div>
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_leaf.svg" />
          <h3>Math</h3>
        </div>
        <p>Your score for math is <b>95%</b> or <b>95/100</b> questions answered correctly. This is <b>great</b>!</p>
      </div>
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_bread.svg" />
          <h3>Math <span class="oi" data-glyph="calculator" title="Calculator" aria-hidden="true"></span></h3>
        </div>
        <p>Your score for math (calculator) is <b>100%</b> or <b>100/100</b> questions answered correctly. This is <b>perfect</b>!</p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1 {
    font-size: 3rem;
    margin-top: 2rem;
  }

  .progress {
    display: flex;
    flex-wrap: wrap;
  }

  .card {
    border: #aaa 1px solid;
    border-radius: 10px;
    padding: 5px 20px;
    margin-right: 20px;
    margin-bottom: 20px;
    width: 250px;
  }
  
  .card > p {
    font-family: 'nunitolight';
    letter-spacing: 0;
    line-height: 20px;
  }

  .card .title-bar {
    display: flex;
    height: 60px;
  }

  .card .title-bar > * {
    margin: 0;
    line-height: 60px;
  }

  .card .title-bar > h3 {
    margin-left: 0.5rem;
  }

  .card .title-bar > img {
    border: #ddd 1px solid;
    border-radius: 50%;
    padding: 2px;
    margin: 7px;
    margin-left: 0;
    width: 40px;
  }
</style>
