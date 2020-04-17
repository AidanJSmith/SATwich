<template>
  <main id="main">
    <section id="sidebar">
      <Sidebar />
    </section>
    <section id="app">
      <router-view></router-view>
    </section>
  </main>
</template>

<script>
  import Sidebar from './components/Sidebar.vue'

  export default {
    name: 'App',
    components: {
      Sidebar
    }
  }
</script>

<style>
  @font-face {
      font-family: 'nunitolight';
      src: url('./assets/fonts/nunito-light-webfont.woff2') format('woff2'),
           url('./assets/fonts/nunito-light-webfont.woff') format('woff');
      font-weight: normal;
      font-style: normal;
  }
  @import url("https://use.typekit.net/eyp4egm.css");
  @import url('./assets/fonts/open-iconic.min.css');

  body {
    height: 100vh;
    margin: 0;
  }

  #main {
    font-family: 'poiret-one', Avenir, Helvetica, Arial, sans-serif;
    letter-spacing: 2px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    display: flex;
    height: 100vh;
  }

  #sidebar {
    box-shadow: #0003 5px 0 10px;
    padding-top: 1rem;
    width: 300px;
    position: relative;
  }

  #app {
    padding-left: 80px;
    padding-top: 1rem;
    flex: 1 1;
  }

  .flex-wrap {
    display: flex;
    flex-wrap: wrap;
  }

  .card {
    border: #aaa 1px solid;
    border-radius: 10px;
    padding: 5px 20px;
    margin-right: 20px;
    margin-bottom: 20px;
  }
  
  .card p {
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
