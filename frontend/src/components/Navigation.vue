<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <ul>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/tasks">Challenges</RouterLink>
            <RouterLink to="/hof">Hall of Fame</RouterLink>
            <RouterLink to="/login">Log in</RouterLink>
        </ul>
    </nav>
</template>