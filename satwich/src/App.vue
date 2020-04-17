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
    height: 100%;
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
    overflow: hidden;
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
    height: 100vh;
    overflow: scroll;
  }
  
  #app::-webkit-scrollbar {
    width: 12px;
  }
  
  #app::-webkit-scrollbar-track {
    background-color: #eee;
    border-radius: 10px;
  }
  
  #app::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 10px;
  }
  
  button {
    background: none;
    border: none;
    border-radius: 50%;
    color: #555;
    font-family: inherit;
    font-size: 1.2rem;
    outline: none;
    transition-duration: 0.2s;
  }

  button:hover {
    border-radius: 5px;
    background-color: #eee;
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

  
  #overlay-full {
    background-color: #0004;
    display: none;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
  }
  
  #overlay-full > div {
    background-color: #fff;
    border-radius: 5px;
    padding: 10px 30px;
    width: 500px;
  }

  form .row {
    display: flex;
    font-family: 'nunitolight';
    letter-spacing: 0;
    line-height: 20px;
  }

  form .row > * {
    flex: 1 1;
  }

  form input, select {
    border: #aaa 1px solid;
    border-radius: 5px;
    font-size: 18px;
    margin-bottom: 15px;
    padding: 5px 10px;
    outline: none;
  }

  form button {
    padding: 20px;
  }

  #time-field {
    display: none;
  }

  #add-profile {
    cursor: pointer;
  }

  .green {
    color: #8cc63f;
  }

  .orange {
    color: #f6b319;
  }
</style>
