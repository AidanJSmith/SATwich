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
            <p>{{item.time==0 ? "N/A" : item.time}}</p>
          </div>
          <div class="overlay-actions">
            <router-link to="/session" class="vflex">
              <span class="oi text-big orange" data-glyph="media-play" title="Resume Test" aria-hidden="true"></span>
              <p><b>Resume Test</b></p>
            </router-link>
            <p class="text-small"><span class="oi" data-glyph="media-stop" title="End Test" aria-hidden="true"></span> End Test</p>
          </div>
        </div>
    </section>
    <h2>Your Profiles <span id="add-profile" class="oi green" data-glyph="plus" title="Add Profile" aria-hidden="true" @click="openAddProfile();"></span></h2>
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
            <p>{{item.time==0 ? "N/A" : item.time}}</p>
          </div>
          <div class="overlay-actions">
            <router-link to="/session" class="vflex">
              <span class="oi text-big green" data-glyph="media-play" title="Start Test" aria-hidden="true"></span>
              <p><b>Start Test</b></p>
            </router-link>
            <p class="text-small"><span class="oi" data-glyph="trash" title="Remove Profile" aria-hidden="true"></span> Remove Profile</p>
          </div>
        </div>
    </section>
    <section id="overlay-full" v-on:click="closeDialog();">
      <div v-on:click="stopPropogation($event);">
        <h2>Add A Profile</h2>
        <br>
        <form>
          <div class="row">
            <label for="name">Name: </label>
            <input id="name" type="text" v-model="name">
          </div>
          <div class="row">
            <label for="test">Test Type: </label>
            <select id="test" v-model="type">
              <option>SAT</option>
            </select>
          </div>
          <div class="row">
            <label for="pdf">Test PDF: </label>
            <select id="pdf" v-model="pdf">
              <option v-for="pdf in pdfs" :key="pdf">{{pdf}}</option>
            </select>
          </div>
          <div class="row">
            <label for="questions">Questions: </label>
            <input id="questions" type="number" v-model="questionNum">
          </div>
          <div class="row">
            <label for="fields">Sections: </label>
            <div class="column">
              <div class="row">
                <label for="reading">Reading </label>
                <input id="reading" type="checkbox" v-model="reading">
              </div>
              <div class="row">
                <label for="writing">Writing </label>
                <input id="writing" type="checkbox" v-model="writing">
              </div>
              <div class="row">
                <label for="math">Math </label>
                <input id="math" type="checkbox" v-model="nocalc">
              </div>
              <div class="row">
                <label for="cmath">Math (calculator) </label>
                <input id="cmath" type="checkbox" v-model="calc">
              </div>
            </div>
          </div>
          <div class="row">
            <label for="istimed">Enable Time Limit: </label>
            <input id="istimed" type="checkbox" v-model="time" v-on:click="toggleTimeField();">
          </div>
          <div id="time-field" class="row">
            <label for="time">Time (Minutes): </label>
            <input id="time" type="number" v-model="time_num" value="0">
          </div>
          <div class="row">
            <button type="submit" @click="addProfile()"><span class="oi green" data-glyph="check" title="Check" aria-hidden="true" /> Add Profile</button>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
  import json from "../data/profiles/profiles.json"
  import json2 from "../data/tests/tests.json"
  export default {
    name: 'Profiles',
    data () {
      return {
        finished:[],
        possible:[],
        pdfs:[],
        name:"",
        type:"",
        pdf:"",
        questionNum:"",
        time:false,
        time_num:0,
        reading:false,
        writing:false,
        nocalc:false,
        calc:false,
      }
    },
    methods: {
      openAddProfile () {
        document.getElementById("overlay-full").style.display = "flex";
      },
      toggleTimeField () {
        var timeField = document.getElementById("time-field");
        if (timeField.style.display === "flex")
          timeField.style.display = "none";
        else
          timeField.style.display = "flex";
      },
      addProfile() {
        const fs = require('fs');
        if (!Object.keys(json).includes(this.name)) {
          let tempJSON=json;
          let fields=[];
          if (this.reading) {
            fields.push("Reading");
          }
          if (this.writing) {
            fields.push("Writing");
          }
          if (this.calc) {
            fields.push("Math (calculator)");
          }
          if (this.nocalc) {
            fields.push("Math");
          }
          tempJSON[this.name]={"name":this.name,"type":this.type,"fields":fields,"qnum":this.questionNum,"time":this.time_num,"finished":true,"pdf":this.pdf};
          try { fs.writeFileSync("src/data/profiles/profiles.json", JSON.stringify(tempJSON), 'utf-8'); }
          catch(e) { alert(e); }
        } 
      },
      closeDialog () {
        document.getElementById("overlay-full").style.display = "none";
      },
      stopPropogation (event) {
        event.stopPropagation();
      },
    }, 
    mounted () {
      for (let item of Object.keys(json)) {
        if (json[item]["finished"]) {
          this.finished.push(json[item]);
        } else {
          this.possible.push(json[item]);
        }
      }
      this.pdfs=json2;
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

  .overlay-actions .vflex {
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-decoration: none;
  }

  .text-big {
    font-size: 40px;
  }

  .text-small {
    font-size: 14px;
    margin: 0;
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
