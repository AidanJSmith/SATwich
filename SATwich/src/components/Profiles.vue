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
          <p><b>SAT:</b> Reading, Math</p>
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
    <h2>Your Profiles</h2>
    <section class="flex-wrap">
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>Lunch Break</h3>
          </div>
          <p><b>SAT:</b> Reading, Math</p>
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
          <p><b>ACT:</b> Math, Math Calc</p>
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
  </div>
</template>

<script>
export default {
  name: 'Profiles'
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
    width: 200px;
    position: relative;
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
