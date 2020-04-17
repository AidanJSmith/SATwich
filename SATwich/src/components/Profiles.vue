<template>
  <div>
    <h1>Testing Profiles</h1>
    <h2>Your Unfinished Tests</h2>
    <section class="flex-wrap">
        <div class="card" v-for="item in possible" :key="item.name">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>{{(item.name)}}</h3>
          </div>
          <p><b>{{item.pdf}}</b></p>
          <p>{{item.fields.join(", ")}}</p>
          <div class="profile-info">
            <span class="oi" data-glyph="question-mark" title="Questions" aria-hidden="true"></span>
            <p>{{item.qnum}}</p>
            <span class="oi" data-glyph="timer" title="Time" aria-hidden="true"></span>
            <p>{{item.time}}</p>
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
        <div class="card" v-for="item in finished" :key="item.name">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Bread" />
            <h3>{{(item.name)}}</h3>
          </div>
          <p><b>{{(item.name)}}</b></p>
          <p>{{item.fields.join(", ")}}</p>
          <div class="profile-info">
            <span class="oi" data-glyph="question-mark" title="Questions" aria-hidden="true"></span>
            <p>{{item.qnum}}</p>
            <span class="oi" data-glyph="timer" title="Time" aria-hidden="true"></span>
            <p>{{item.time}}</p>
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
import json from "../data/profiles/profiles.json"
export default {
  name: 'Profiles',
  data() {
    return {
      finished:[],
      possible:[],
    }
  }, mounted () {
    let parse=JSON.parse(json);
    for (let item of Object.keys(parse)) {
      if (parse[item]["finished"]) {
        this.finished.push(parse[item])
      } else {
        this.possible.push(parse[item])
      }
    }
  },
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
