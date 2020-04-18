<template>
  <div>
    <h1>Test - {{ this.$route.params.id }}</h1>
    <section class="flex">
      <h2>Section: {{ section }}</h2>
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
          <p>Show Original PDF Pages</p>
          <p class="passage" v-html="passage"></p>
        </div>
      </section>
      <section class="q-wrapper">
        <div class="card question">
          <h2>Question #{{qnum}}</h2>
          <p>{{choices.split("A)")[0]}}</p>
          <div id="answers">
            <label class="container" @click="resetOtherChoices(1)"><b>{{choices.split("A)")[1].split("B)")[0]}}</b>
              <input id="1" data-letter="A" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(2)"><b>{{choices.split("B)")[1].split("C)")[0]}}</b>
              <input id="2" data-letter="B" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(3)"><b>{{choices.split("C)")[1].split("D)")[0]}}</b>
              <input id="3" data-letter="C" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
            <label class="container" @click="resetOtherChoices(4)"><b>{{choices.split("D)")[1]}}</b>
              <input id="4" data-letter="D" type="radio" class="choice">
              <span class="checkmark"></span>
            </label>
          </div>
          <div id="controls" class="controls">
            <button @click="checkAnswer()"><b>Submit</b></button>
          </div>
          <br>
          <div id="results" class="results">
            <h2 id="feedback-text">{{ this.feedbackText }}</h2>
            <button @click="getNextQuestion()"><b>Next Question</b></button>
          </div>
          <br>
        </div>
      </section>
    </section>
    <section id="overlay-full">
      <LoadingAnimation />
    </section>
  </div>
</template>

<script>
import json from "../data/profiles/profiles.json"
import LoadingAnimation from "./LoadingAnimation.vue"

export default {
  name: 'TestSession',
  components: {
    LoadingAnimation,
  },
  data() {
    return {
      section: "Reading",
      qnum: 1,
      choices:"A)B)C)D)",
      passage:"Please wait.",
      pages:[],
      feedbackText: "Incorrect"
    }
  },
  mounted() {
    document.getElementById("sidebar").classList.add("collapsed");
    this.updateData(); 
  }, 
  methods: {
    resetOtherChoices(t) {
      document.querySelectorAll(".choice").forEach((x) => x.checked = false);
      var clickedNode = document.getElementById(t);
      if (clickedNode) clickedNode.checked = true;
    },
    updateData() {
      const fs = require("fs");
      let data = JSON.parse(fs.readFileSync(`src/data/tests/${json[this.$route.params.id]["pdf"]}/test.json`).toString());
      data = JSON.parse(data);
      let reading = data["reading"];           // Get reading section
      for (let key of Object.keys(reading)) {
          let set = reading[key];              // Get set of questions, passage, etc
          this.passage = set[0].replace(/\n/g,"\t\t     <br/>").slice(45,);               // Get the passage text
          this.pages =   set[2];               // Get the pages the text can be found on
          for (let question_key of Object.keys(set[1]))
             if (question_key == this.qnum+1)  // If question matches current one, get answer choices
               this.choices= set[1][question_key];
          if (this.choices!="A)B)C)D)") break; // Go to Writing section
      }
      if (this.choices!="A)B)C)D)") console.log("TIME TO GO TO NEXT SECTION"); // Go to Writing section
    },
    checkAnswer() {
      const fs = require("fs");
      let data = JSON.parse(fs.readFileSync(`src/data/tests/${json[this.$route.params.id]["pdf"]}/test.json`).toString());
      data = JSON.parse(data);
      let answer_key = data["key"];
      if (answer_key["reading"][this.qnum-1] == document.querySelector("input.choice:checked").getAttribute("data-letter")) {
        this.feedbackText = "Correct";
        document.getElementById("feedback-text").style.backgroundColor = "#8cc63f77";
      }
      else {
        this.feedbackText = "Incorrect";
        document.getElementById("feedback-text").style.backgroundColor = "#f36b5755";
      }

      document.getElementById("controls").style.height = 0;
      document.getElementById("results").style.height = "150px";
    },
    getNextQuestion() {
      document.getElementById("controls").style.height = "unset";
      document.getElementById("results").style.height = 0;
      this.resetOtherChoices(0);
      this.qnum++;
      this.updateData();
    }
  },
  beforeDestroy() {
    document.getElementById("sidebar").classList.remove("collapsed");
  }
}
</script>

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
    line-height: 1.8rem;
  }

  .question {
    position: sticky;
    top: 0;
    flex: none;
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
    overflow: hidden;
  }

  .controls button, .results button {
    border: #aaa 1px solid;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    flex: 1 1;
    line-height: 2rem;
  }

  .results {
    transition-duration: 0.5s;
    text-align: center;
    height: 0;
    overflow: hidden;
  }

  #feedback-text {
    padding: 1rem 0;
    border-radius: 3px;
    margin-top: 0;
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
