<template>
  <div>
    <h1>Dashboard</h1>
    <h2>Your Progress</h2>
    <section class="progress">
      <div class="card">
        <div class="title-bar">
          <img src="../assets/img/snd_bread.svg" />
        </div>
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
    border: #ddd 1px solid;
    border-radius: 10px;
    width: 300px;
  }
</style>
