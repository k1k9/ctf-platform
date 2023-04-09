<script>
export default{
    data(){
        return{
            task:{
                "id":1,
                "title": "Example task",
                "level": "easy",
                "category": "Forensics",
                "points": 20,
                "author": "k1k9",
                "solves": 12,
                "rating": 4.23
            }
        }
    }
}
</script>
<template>
    <article>
        <header>
            <h3>{{ this.task.title }}</h3>
            <span class="category" :class="this.task.level">{{this.task.level}}</span>
        </header>
    </article>
</template>