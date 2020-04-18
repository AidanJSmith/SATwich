<template>
  <nav id="nav">
    <ul class="nav-group">
      <li>
        <router-link to="/">
          <button class="nav-button">
            <div class="nav-icon"><img src="../assets/img/snd.svg" alt="Home" /></div>
            <span class="hidden">Dashboard</span>
          </button>
        </router-link>
      </li>
    </ul>
    <hr>
    <ul class="nav-group">
      <li>
        <router-link to="/Tests">
          <button class="nav-button">
            <div class="nav-icon"><span class="oi red" data-glyph="book" title="Your Tests" aria-hidden="true"></span></div>
            <span class="hidden">Your Test PDFs</span>
          </button>
        </router-link>
      </li>
      <li>
        <router-link to="/Profiles">
          <button class="nav-button">
            <div class="nav-icon"><span class="oi orange" data-glyph="pencil" title="Profiles" aria-hidden="true"></span></div>
            <span class="hidden">Test Profiles</span>
          </button>
        </router-link>
      </li>
      <li>
        <router-link to="/Analytics">
          <button class="nav-button">
            <div class="nav-icon"><span class="oi gold" data-glyph="graph" title="Analytics" aria-hidden="true"></span></div>
            <span class="hidden">Test Analytics</span>
          </button>
        </router-link>
      </li>
    </ul>
    <hr>
    <section class="footer">
      <p class="hidden">v0.0.1</p>
      <div class="group-right">
        <button>
          <span class="oi" data-glyph="cog" title="Settings" aria-hidden="true"></span>
        </button>
        <button v-on:click="collapseSidebar()">
          <span class="oi" data-glyph="chevron-left" title="Collapse" aria-hidden="true"></span>
        </button>
      </div>
    </section>
  </nav>
</template>

<script>
  export default {
    name: 'Sidebar',
    methods: {
      collapseSidebar() {
        if (document.getElementById("sidebar").classList.contains("collapsed"))
          document.getElementById("sidebar").classList.remove("collapsed");
        else
          document.getElementById("sidebar").classList.add("collapsed");
      }
    }
  }
</script>

<style scoped>
  .nav-button {
    padding: 1rem;
    line-height: 1rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-align: left;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
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

  .collapsed #nav {
    padding: 1rem;
  }

  .collapsed #nav .nav-group {
    padding: 0;
  }
  .collapsed .nav-button {
    display: flex;
    justify-content: center;
    padding: 1rem 0.5rem !important;
    width: 100%;
  }

  .collapsed .nav-icon {
    margin: 0;
  }

  #sidebar.collapsed hr {
    width: 100%;
    margin: auto;
  }

  .collapsed .footer {
    padding-left: 2px;
  }

  .collapsed .footer .group-right {
    display: flex;
  }

  .collapsed > * .hidden {
    display: none !important;
  }
</style>