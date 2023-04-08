<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <header>
        <h1>CTF-CM</h1>

        <nav>
            <ul>
                <RouterLink to="/">Home</RouterLink>
                <RouterLink to="/tasks">Challenges</RouterLink>
                <RouterLink to="/hof">Hall of Fame</RouterLink>
                <RouterLink to="/login">Log in</RouterLink>
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
}
</style>