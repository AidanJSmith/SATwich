<template>
  <div>
    <h1>Test - {{ this.$route.params.id }}</h1>
    <section class="flex">
      <h2>Section: </h2>
      <section class="flex right">
        <div>
          <span class="oi orange" data-glyph="media-pause" title="Stop Test" aria-hidden="true"></span>
          <b>Pause Test</b>
        </div>
        <div>
          <span class="oi red" data-glyph="media-stop" title="Stop Test" aria-hidden="true"></span>
          <b>Stop Test</b>
        </div>
      </section>
    </section>
    <section class="flex">
      <section class="flex-big">
        <div class="card">
          <h2>Passage</h2>
          <p>Show Original PDF Page</p>
          <p class="passage">{{this.passage}}</p>
        </div>
      </section>
      <section>
        <div class="card question">
          <h2>Question #{{qnum}}</h2>
          <p>{{choices.split("A)")[0]}}</p>
          <div id="answers">
            <label class="container" @click="resetOtherChoices(1)"><b>Option One</b>
              <input id="1" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(2)"><b>Option Two</b>
              <input id="2" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(3)"><b>Option Three</b>
              <input id="3" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(4)"><b>Option Four</b>
              <input id="4" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
          </div>
        </div>
        <div class="controls">
          <button><b>Submit</b></button>
        </div>
      </section>
    </section>
  </div>
</template>

<script>
import json from "../data/profiles/profiles.json"

export default {
  name: 'TestSession',
  data() {
    return {
      qnum: 38,
      choices:"A)B)C)D)",
      passage:"Please wait.",
      pages:[],
    }
  },
  mounted() {
    document.getElementById("sidebar").classList.add("collapsed");
    this.updateData(); 
  }, methods: {
    resetOtherChoices(t) {
      document.querySelectorAll(".choice").forEach((x) => x.checked = false); // lol it just prevents anything from being clicked ig
      document.getElementById(t).checked = true;
    },
    updateData() {
      const fs = require("fs");
      let data =(JSON.parse(fs.readFileSync(`src/data/tests/${json[this.$route.params.id]["pdf"]}/test.json`).toString()));
      data = JSON.parse(data);
      for (let key of Object.keys(data["reading"])) {
          if (this.choices!="A)B)C)D)") {
            break;
          }
          this.passage=data["reading"][key][0];
          this.pages=data["reading"][key][2];
          for (let question_key of Object.keys(data["reading"][key][1])) {
             if (question_key==this.qnum+1) {
               this.choices=data["reading"][key][1][question_key];
             }
          }
      }
      if (this.choices!="A)B)C)D)") {
          console.log("TIME TO GO TO NEXT SECTION");
      }

    }
  },
  beforeDestroy() {
    document.getElementById("sidebar").classList.remove("collapsed");
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1 {
    font-size: 3rem;
    margin-top: 2rem;
  }

  .flex {
    display: flex;
    padding-right: 50px;
  }

  .flex > * {
    display: flex;
    flex-direction: column;
    flex: 1 1;
  }

  .flex-big {
    flex: 2 1;
  }

  .right {
    flex: none;
    flex-direction: row;
    justify-content: right;
    align-items: center;
  }

  .right > div {
    display: flex;
    flex-direction: row;
    align-items: center;
    min-width: 150px;
  }

  .oi {
    font-size: 1.5rem;
    margin-right: 1rem;
  }

  .card {
    flex: 1 1;
  }

  .passage {
    font-size: 1.3rem;
  }

  .question p {
    font-family: 'nunitolight', inherit;
    font-size: 1.2rem;
    line-height: 1.8rem;
  }
  
  .question #answers label {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }

  .controls {
    display: flex;
    flex-direction: row;
    padding-right: 20px;
  }

  .controls button {
    border: #aaa 1px solid;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    flex: 1 1;
    line-height: 2rem;
  }
  
  /* Customize the label (the container) */
  .container {
    display: block;
    position: relative;
    padding-left: 35px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  /* Hide the browser's default radio button */
  .container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
  }

  /* Create a custom radio button */
  .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-radius: 50%;
  }

  /* On mouse-over, add a grey background color */
  .container:hover input ~ .checkmark {
    background-color: #ccc;
  }

  /* When the radio button is checked, add a blue background */
  .container input:checked ~ .checkmark {
    background-color: #2196F3;
  }

  /* Create the indicator (the dot/circle - hidden when not checked) */
  .checkmark:after {
    content: "";
    position: absolute;
    display: none;
  }

  /* Show the indicator (dot/circle) when checked */
  .container input:checked ~ .checkmark:after {
    display: block;
  }

  /* Style the indicator (dot/circle) */
  .container .checkmark:after {
    top: 9px;
    left: 9px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: white;
  }
</style>
