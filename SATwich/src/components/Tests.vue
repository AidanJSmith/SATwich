<template>
  <div>
    <h1>Your Test PDFs</h1>
    <h2>Your Test PDFs <span id="add-profile" class="oi green" data-glyph="plus" title="Add Profile" aria-hidden="true" @click="openDialog();"></span></h2>
    <section class="flex-wrap">
        <div class="card">
          <div class="title-bar">
            <img src="../assets/img/snd.svg" alt="Sandwich" />
            <h3>Test PDF Name</h3>
          </div>
          <p><b>Test Type</b></p>
          <p>69 Questions</p>
          <div class="overlay-actions">
            <p class="text-small"><span class="oi" data-glyph="trash" title="Remove Profile" aria-hidden="true"></span> Delete PDF</p>
          </div>
        </div>
    </section>
    <section id="overlay-full" v-on:click="closeDialog();">
      <div v-on:click="stopPropogation($event);">
        <h2>Add A PDF</h2>
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
            <input id="pdf" type="file" accept=".pdf">
          </div>
          <div id="time-field" class="row">
            <label for="time">Time (Minutes): </label>
            <input id="time" type="number" v-model="time_num" value="0">
          </div>
          <div class="row">
            <button type="submit" @click="addPDF()"><span class="oi green" data-glyph="check" title="Check" aria-hidden="true" /> Add PDF</button>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
    name: 'Tests',
    methods: {
      openDialog () {
        document.getElementById("overlay-full").style.display = "flex";
      },
      closeDialog () {
        document.getElementById("overlay-full").style.display = "none";
      },
      stopPropogation (event) {
        event.stopPropagation();
      },
    }, 
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1 {
    font-size: 3rem;
    margin-top: 2rem;
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
