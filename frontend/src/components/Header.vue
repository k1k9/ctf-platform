<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <header>
        <RouterLink to="/">
            <h1>CTF-CM</h1>
        </RouterLink>

        <nav>
            <ul>
                <li><RouterLink to="/">Home</RouterLink></li>
                <li><RouterLink to="/tasks">Challenges</RouterLink></li>
                <li><RouterLink to="/hof">Hall of Fame</RouterLink></li>
                <li><RouterLink to="/login">Log in</RouterLink></li>
            </ul>
        </nav>
    </header>
</template>

<style lang="scss" scoped>
header{
    width: 100%;
    padding: 0;
    margin: 0;
    text-align: center;

    a{
        text-decoration: none;
    }

    nav{
        width: 100%;
        ul{
            display: flex;
            justify-content: center;
            gap: 1rem;
            padding: 0;
            margin: 0;
            list-style: none;
        }
    }
}
@media (min-width: 993px){
  header{
    display: flex;
    box-sizing: border-box;
    overflow: hidden;
    text-align: left;
    justify-content: space-between;
    align-items: center;
    padding: .5rem 1rem;

    nav{
        width: auto;
    }
  }
}
</style>