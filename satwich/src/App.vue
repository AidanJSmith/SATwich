<template>
  <main id="main">
    <section id="sidebar">
      <Sidebar />
    </section>
    <section id="app">
      <Dashboard />
    </section>
  </main>
</template>

<script>
  import Dashboard from './components/Dashboard.vue'
  import Sidebar from './components/Sidebar.vue'

  export default {
    name: 'App',
    components: {
      Dashboard,
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
</style>
