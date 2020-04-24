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
  /* Import SASS compiled styles */
  @import './css/main.css';

  ::selection {
    background-color: #fdca92;
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
</style>
