<script>
import TaskCard from '../components/TaskCard.vue';
import axios from 'axios';
export default{
  components:{
    TaskCard
  },

  data(){
    return{
      tasks: []
    }
  },
  mounted(){
    axios
        .get(`http://localhost:9999/tasks/`)
        .then(response => (this.tasks = response["data"]))
  }
}
</script>

<template>
  <section>
    <header class="section-header">
      <h2>All challenges</h2>

      <div class="filtering">
        <div class="filtering__category">
          <label for="category">Category: </label>
          <select name="category" id="category">
            <option value="all">All</option>
            <option value="web">Web</option>
            <option value="binary">Binary</option>
            <option value="forensics">Forensics</option>
            <option value="cryptography">Cryptography</option>
            <option value="miscellaneous">Miscellaneous</option>
            <option value="reverse-engineering">Reverse Engineering</option>
          </select>
        </div>

        <div class="filtering__level">
          <label for="level">Level: </label>
          <select name="level" id="level">
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
            <option value="unrated">Unrated</option>
          </select>
        </div>

        <div class="filtering__order">
          <label for="order">Order: </label>
          <select name="order" id="order">
            <option value="highest-rating">Highest rating</option>
            <option value="most-solves">Most solves</option>
            <option value="least-solves">Least solves</option>
          </select>
        </div>
      </div>
    </header>

    <main>
      <TaskCard v-for="task in tasks" :data="task"/>
    </main>
  </section>
</template>
  
<style lang="scss" scoped>
@import '../assets/variables';

section {
  width: 100%;
  min-height: 100vh;
  margin-top: 10vh;
  padding: 0 1rem;
  box-sizing: border-box;
  overflow-y: hidden;

  .show-filters {
    width: 100%;
    background: $background-alt;
    color: $foreground;
    font-size: 1rem;
    outline: none;
    border: 1px solid $gray;
    padding: .5rem;
  }

  .filtering {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 2rem 1rem;
    box-sizing: border-box;
    overflow: hidden;

    div {
      display: flex;
      flex-direction: column;

      label {
        font-size: 1rem;
        font-weight: 700;
        padding-bottom: 0.5rem;
      }

      select {
        background: $background-alt;
        color: $foreground;
        border: 1px solid $gray;
        padding: .5rem;
        font-size: 1rem;
      }
    }
  }

  main {
    display: grid;
    padding-top: 5vh;
    grid-template-columns: 1fr;
    gap: 5vh;
  }
}


@media (min-width: 993px) {
  section {
    header {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;

      h2{
        margin:0;
        min-width: 280px;
      }

      .filtering {
        flex-direction: row;
        justify-content: flex-end;
        padding: 0;
      }
    }

    main{
      grid-template-columns: repeat(2, 1fr);
    }
  }
}

@media (min-width: 1200px){
section{
  main{
    grid-template-columns: repeat(2, 1fr);
  }
}
}
</style>