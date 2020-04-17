<template>
  <div>
    <h1>Testing Profiles</h1>
    <h2>Your Unfinished Tests</h2>
    <section class="flex-wrap">
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>Lunch Break</h3>
          </div>
          <p><b>SAT Test 1</b></p>
          <p>Reading, Math, Math Calc</p>
          <div class="profile-info">
            <span class="oi" data-glyph="question-mark" title="Questions" aria-hidden="true"></span>
            <p>16</p>
            <span class="oi" data-glyph="timer" title="Time" aria-hidden="true"></span>
            <p>15.2</p>
          </div>
          <div class="overlay-actions">
            <span class="oi text-big orange" data-glyph="media-play" title="Resume Test" aria-hidden="true"></span>
            <p><b>Resume Test</b></p>
            <p class="text-small"><span class="oi" data-glyph="media-stop" title="End Test" aria-hidden="true"></span> End Test</p>
          </div>
        </div>
    </section>
    <h2>Your Profiles <span class="oi green" data-glyph="plus" title="Add Profile" aria-hidden="true" v-on:click="openAddProfile();"></span></h2>
    <section class="flex-wrap">
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>Lunch Break</h3>
          </div>
          <p><b>SAT Test 1</b></p>
          <p>Reading, Math, Math Calc</p>
          <div class="profile-info">
            <span class="oi" data-glyph="question-mark" title="Questions" aria-hidden="true"></span>
            <p>25</p>
            <span class="oi" data-glyph="timer" title="Time" aria-hidden="true"></span>
            <p>35</p>
          </div>
          <div class="overlay-actions">
            <span class="oi text-big green" data-glyph="media-play" title="Start Test" aria-hidden="true"></span>
            <p><b>Start Test</b></p>
            <p class="text-small"><span class="oi" data-glyph="trash" title="Remove Profile" aria-hidden="true"></span> Remove Profile</p>
          </div>
        </div>
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>Other One</h3>
          </div>
          <p><b>Reddit ACT 1</b></p>
          <p>Math, Math Calc</p>
          <div class="profile-info">
            <span class="oi" data-glyph="question-mark" title="Questions" aria-hidden="true"></span>
            <p>55</p>
            <span class="oi" data-glyph="timer" title="Time" aria-hidden="true"></span>
            <p>45</p>
          </div>
          <div class="overlay-actions">
            <span class="oi text-big green" data-glyph="media-play" title="Start Test" aria-hidden="true"></span>
            <p><b>Start Test</b></p>
            <p class="text-small"><span class="oi" data-glyph="trash" title="Remove Profile" aria-hidden="true"></span> Remove Profile</p>
          </div>
        </div>
    </section>
    <section id="overlay-full" v-on:click="closeDialog();">
      <div v-on:click="stopPropogation($event);">
        <h2>Add A Profile</h2>
        <br>
        <form action="idk lol">
          <div>
            <label for="name">Name: </label>
            <input id="name" type="text">
          </div>
          <div>
            <label for="test">Test Type: </label>
            <select id="test">
              <option>SAT</option>
            </select>
          </div>
          <div>
            <label for="test">Test PDF: </label>
            <select id="test">
              <option>option 1</option>
            </select>
          </div>
          <div>
            <label for="questions">Questions: </label>
            <input id="questions" type="number">
          </div>
          <div>
            <label for="istimed">Enable Time Limit: </label>
            <input id="istimed" type="checkbox" v-on:click="toggleTimeField();">
          </div>
          <div id="time-field">
            <label for="time">Time (Minutes): </label>
            <input id="time" type="number" value="0">
          </div>
          <div>
            <button type="submit"><span class="oi green" data-glyph="check" title="Check" aria-hidden="true" /> Add Profile</button>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
    name: 'Profiles',
    methods: {
      openAddProfile () {
        document.getElementById("overlay-full").style.display = "flex";
      },
      toggleTimeField() {
        var timeField = document.getElementById("time-field");
        if (timeField.style.display === "flex")
          timeField.style.display = "none";
        else
          timeField.style.display = "flex";
      },
      closeDialog () {
        document.getElementById("overlay-full").style.display = "none";
      },
      stopPropogation (event) {
        event.stopPropagation();
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

  form > div {
    display: flex;
    font-family: 'nunitolight';
    letter-spacing: 0;
    line-height: 20px;
  }

  form > div > * {
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
    width: 200px;
    position: relative;
  }

  .card > p {
    margin-top: 10px;
    margin-bottom: 20px;
  }

  .card .title-bar > h3 {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .profile-info {
    display: flex;
    margin-bottom: 10px;
  }

  .profile-info > * {
    flex: 1 1;
    margin: 0;
  }

  .card:hover .overlay-actions {
    display: flex;
    animation: show-actions 0.2s forwards;
  }

  .overlay-actions {
    background-color: #fdca92;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
  }

  .text-big {
    font-size: 40px;
  }

  .text-small {
    font-size: 14px;
    margin: 0;
  }

  .green {
    color: #8cc63f;
  }

  .orange {
    color: #f6b319;
  }

  @keyframes show-actions {
    0% {
      border-radius: 50%;
      opacity: 0;
    }

    100% {
      border-radius: inherit;
      opacity: 1;
    }
  }
</style>
