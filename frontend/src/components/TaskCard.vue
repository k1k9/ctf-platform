<script>
import { useRouter } from 'vue-router';
export default{
    props:{
        data:{
            type: Object,
            required: true,
        }
    },
    methods:{
        redicrectToTask(){
            this.$router.push("/tasks/"+this.data.id);
        }
    }
}
</script>

<template>
    <article @click="redicrectToTask">
        <header>
            <h3>{{ data.title }}</h3>
            <span class="category" :class="data.lvl">{{data.lvl}}</span>
        </header>

        <main>
            <p>- Category: {{ data.category }}</p>
            <p>- Points: {{ data.reward }}</p>
            <p>- Author: {{ data.author }}</p>
            <p>- Solves: {{ data.solvers }}</p>
            <p>- Rating: {{ data.rating }}</p>

        </main>
    </article>
</template>

<style lang="scss" scoped>
@import '../assets/variables';
article{
    background: $background-alt;
    box-sizing: border-box;
    overflow: hidden;
    padding: 1rem;
    border-radius: 5px;
    transition: opacity .5s;

    &:hover{
        cursor: pointer;
        opacity: 0.5;
    }

    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-sizing: border-box;
        gap: 1rem;
        h3{
            font-size: 1rem;
            color: $foreground;
        }
        .category{
            background: $gray;
            color: $foreground;
            padding: 5px 10px;
            border-radius: 1px;
        }
        .category.easy{background: $green;}
        .category.medium{background: $yellow;}
        .category.hard{background: $red;}
    }

    main{
        font-family: "Hack";
        line-height: 0.7rem;
        font-size: 0.9rem;
        color: $gray;
    }
}
</style>