<template>
  <nav id="nav">
    <ul class="nav-group">
      <li><button class="nav-button"><span class="oi" data-glyph="home" title="Home" aria-hidden="true"></span>Dashboard</button></li>
    </ul>
    <hr>
    <ul class="nav-group">
      <li><button class="nav-button"><span class="oi red" data-glyph="book" title="Book" aria-hidden="true"></span>Your Tests</button></li>
      <li><button class="nav-button"><span class="oi orange" data-glyph="pencil" title="Pencil" aria-hidden="true"></span>Test Profiles</button></li>
      <li><button class="nav-button"><span class="oi purple" data-glyph="graph" title="Graph" aria-hidden="true"></span>Test Analytics</button></li>
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

  .nav-button .oi {
    margin-right: 1rem;
  }

  .nav-button:hover {
    border-radius: 5px;
    background-color: #eee;
  }

  #nav {
    padding: 0 1rem;
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
    margin: 1.5rem;
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