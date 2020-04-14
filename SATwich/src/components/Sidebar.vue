<template>
  <nav id="nav">
    <ul class="nav-group">
      <li><button class="nav-button"><div class="nav-icon"><img src="../assets/img/snd.svg" /></div><span class="jank">Dashboard</span></button></li>
    </ul>
    <hr>
    <ul class="nav-group">
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi red" data-glyph="book" title="Book" aria-hidden="true"></span></div>Your Tests</button>
      </li>
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi orange" data-glyph="pencil" title="Pencil" aria-hidden="true"></span></div>Test Profiles</button>
      </li>
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi purple" data-glyph="graph" title="Graph" aria-hidden="true"></span></div>Test Analytics</button>
      </li>
    </ul>
    <hr>
  </nav>
</template>

<script>
  export default {
    name: 'Sidebar'
  }
</script>

<style scoped>
  .nav-button {
    background: none;
    border: none;
    border-radius: 50%;
    color: #555;
    font-family: inherit;
    font-size: 1.3rem;
    font-weight: 600;
    letter-spacing: 2px;
    padding: 1rem;
    line-height: 1rem;
    text-align: left;
    width: 100%;
    outline: none;
    transition-duration: 0.1s;
  }

  .nav-button:hover {
    border-radius: 5px;
    background-color: #eee;
  }

  .nav-icon {
    display: inline-block;
    margin-right: 1rem;
    width: 30px;
    vertical-align: bottom;
  }

  .nav-icon > * {
    display: block;
    margin: auto;
    width: 20px;
  }

  .nav-icon > img {
    width: 30px;
  }

  #nav {
    padding-left: 0.5rem;
    padding-right: 2rem;
  }

  #nav .nav-group {
    list-style: none;
    padding-left: 1rem;
    margin-bottom: 1rem;
  }

  #nav hr {
    border-style:solid;
    color:#ddd; 
    width: 200px;
    margin: 2rem;
  }

  .red {
    color: #FF000A;
  }

  .orange {
    color: #FFA000;
  }

  .purple {
    color: #B200FF;
  }
</style>