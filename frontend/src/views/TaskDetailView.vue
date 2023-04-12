<script>
import axios from 'axios';
import IconDownload from '../components/icons/IconDownload.vue';

export default {
    components:{
        IconDownload
    },
    data() {
        return {
            task: []
        }
    },
    mounted(){
        const taskId = this.$route.params.id;
        axios
            .get(`http://localhost:9999/task/${taskId}`)
            .then(response => (this.task = response["data"]))
    }
}
</script>
<template>
    <article>
        <main>
            <div class="header">
                <p>challenge.txt</p>
            </div>

            <div class="content">
                <h5>{{ this.task.title }}</h5>
                {{ this.task.content }}
            </div>

            <div class="footer">
                <div v-if="this.task.file" class="download_file">
                    <a :href="'/public/' + this.task.file">
                        <IconDownload/>
                        {{ this.task.file }}
                    </a>
                </div>

                <div class="entry_flag">
                    <input type="text" placeholder="CTFCM{h4ck3rm4n}">
                    <input type="submit" value="Submit">
                </div>
            </div>
        </main>

        <aside>
            <div class="metadata">
                <div class="heading">
                    <p>metadata.txt</p>
                </div>
                <ul class="content">
                    <li>- Category: {{ this.task.category }}</li>
                    <li>- Level: {{ this.task.lvl }}</li>
                    <li>- Points: {{ this.task.reward }}</li>
                    <li>- Author: {{ this.task.author }}</li>
                    <li>- Solves: {{ this.task.solvers }}</li>
                    <li>- Rating: {{ this.task.rating }}</li>
                </ul>
            </div>

            <div class="solutions">
                <div class="heading">
                    <p>may_help.txt</p>
                </div>
                <ul class="content">
                    <li>- <a href="#">The basics of crypto</a></li>
                    <li>- <a href="#">Base64 Wikipedia</a></li>
                    <li>- <a href="#">CyberChef</a></li>
                </ul>
            </div>
        </aside>
    </article>
</template>

<style lang="scss" scoped>
@import '../assets/variables';

article {
    width: 80%;
    margin: 0 auto;
    display: grid;
    box-sizing: border-box;
    margin-top: 5vh;
    gap: 2rem;
    font-family: "Hack";

    main {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        background-color: $background-alt;
        padding-bottom: 0.8rem;
        min-height: 300px;

        .header{
            width: 100%;
            background: $background-alt2;
            color: #3f3f3f;
            padding: .3rem .5rem;
            box-sizing: border-box;
            p{
                margin: 0;
            }
        }
        .content{
            padding: 0.8rem;
        }
        .footer {
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-top: 1rem;
            width: 100%;
            margin-top: auto;
            gap: 2rem;

            .download_file{
                box-sizing: border-box;
                padding: 0.3rem;
                
                a{
                    display: flex;
                    align-items: center;
                    color: $foreground;
                    text-decoration: none;
                    gap: 0.5rem;
                    transition: opacity .5s;

                    &:hover{
                        cursor: pointer;
                        opacity: 0.2;
                    }
                }
            }

            .entry_flag{
                display: flex;
                justify-content: center;
                
                input[type=text] {
                    background: $background;
                    color: $foreground;
                    border: none;
                    padding: .5rem;

                    &::placeholder {
                        opacity: 0.7;
                        color: $foreground;
                    }
                }

                input[type=submit] {
                    background: $background;
                    border: none;
                    color: $foreground;
                    transition: background .5s, color .5s;

                    &:hover{
                        cursor: pointer;
                        background: $foreground;
                        color: $background
                    }
                }
            }
        }
    }

    aside {
        display: grid;
        box-sizing: border-box;

        .metadata,
        .solutions {
            box-sizing: border-box;
            background-color: $background-alt;

            .heading {
                width: 100%;
                background: $background-alt2;
                color: #3f3f3f;
                padding: .3rem .5rem;
                box-sizing: border-box;

                p {
                    margin: 0;
                }
            }

            ul.content {
                width: 100%;
                box-sizing: border-box;
                list-style: none;
                padding: 0 .8rem;
                color: $gray;

                a {
                    color: $gray;
                }

                li {
                    padding: .3rem 0 .3rem 0;
                }
            }

        }
    }
}

@media (min-width: 600px){
    article{
        main{

            .content{
                padding: 1.2rem;
            }
            
            .footer{
                padding: 1rem;
                box-sizing: border-box;
                .entry_flag{
                    input[type=text]{
                        width: 80%;
                    }
                    input[type=submit]{
                        width: 20%;
                    }
                }
            }
        }
    }
}

@media (min-width: 993px)  {
    article{
        grid-template-columns: repeat(2, 1fr);

            aside{
            gap: 2rem;
        }
    }
}

</style>