<script setup>
import { RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue';
</script>

<template>
  <header>
      <h1>CTF-CM</h1>

      <Navigation/>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style lang="scss" scoped>

</style>
