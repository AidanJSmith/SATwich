<template>
  <nav id="nav">
    <ul class="nav-group">
      <li>
        <router-link to="/">
          <button class="nav-button"><div class="nav-icon"><img src="../assets/img/snd.svg" alt="Home" /></div>Dashboard</button>
        </router-link>
      </li>
    </ul>
    <hr>
    <ul class="nav-group">
      <li>
        <router-link to="Tests">
          <button class="nav-button"><div class="nav-icon"><span class="oi red" data-glyph="book" title="Your Tests" aria-hidden="true"></span></div>Your Test PDFs</button>
        </router-link>
      </li>
      <li>
        <router-link to="Profiles">
          <button class="nav-button"><div class="nav-icon"><span class="oi orange" data-glyph="pencil" title="Profiles" aria-hidden="true"></span></div>Test Profiles</button>
        </router-link>
      </li>
      <li>
        <router-link to="Analytics">
          <button class="nav-button"><div class="nav-icon"><span class="oi gold" data-glyph="graph" title="Analytics" aria-hidden="true"></span></div>Test Analytics</button>
        </router-link>
      </li>
    </ul>
    <hr>
    <ul class="nav-group">
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi" data-glyph="pin" title="Pinned Profile" aria-hidden="true"></span></div>Pinned</button>
      </li>
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi" data-glyph="pin" title="Pinned Profile" aria-hidden="true"></span></div>Pinned</button>
      </li>
      <li>
        <button class="nav-button"><div class="nav-icon"><span class="oi" data-glyph="pin" title="Pinned Profile" aria-hidden="true"></span></div>Pinned</button>
      </li>
    </ul>
    <section class="footer">
      <p>v0.0.1</p>
      <div class="group-right">
        <button>
          <span class="oi" data-glyph="cog" title="Settings" aria-hidden="true"></span>
        </button>
        <button>
          <span class="oi" data-glyph="chevron-left" title="Collapse" aria-hidden="true"></span>
        </button>
      </div>
    </section>
  </nav>
</template>

<script>
  export default {
    name: 'Sidebar'
  }
</script>

<style scoped>
  .nav-button {
    padding: 1rem;
    line-height: 1rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-align: left;
    width: 100%;
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
    width: 80%;
    margin: 2rem;
  }

  .oi {
    color: #777;
  }

  .red {
    color: #FF000A;
  }

  .orange {
    color: #F36B57;
  }

  .gold {
    color: #FFA000;
  }

  .footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 0.5rem 1rem;
    padding-left: 3rem;
    height: 50px;
    font-size: 16px;
    display: flex;
    align-items: center;
  }

  .footer .group-right {
    font-size: 30px;
    flex: 1 1;
    text-align: right;
  }

  .footer .group-right button {
    margin-left: 0.5rem;
    padding: 0.5rem;
    line-height: 10px;
  }
</style>