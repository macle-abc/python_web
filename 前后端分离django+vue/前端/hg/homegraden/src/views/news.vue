<template>
    <div>
        <div style="display: none">
            {{this.$store.state.list}}
        </div>
        <my_section>
            <div slot="content">
                <div v-if="this.type === 'home'">
                    <div align="center" style="border-bottom: 2px solid rgba(201,202,202,0.99)">
                        <h2>{{GetCurrentTitle}}</h2>
                        <time>{{GetCurrentNewsTime}}</time>
                    </div>
                    <div>
                        <p>{{GetCurrentContent}}</p>
                    </div>
                    <div>
                        <span>上一条: </span>
                        <b-button :disabled="prev_is_disabled" pill variant="outline-success" @click="prev">
                            {{GetPrevTitle}}
                        </b-button>
                        <br/>
                        <span>下一条: </span>
                        <b-button :disabled="next_is_disabled" pill variant="outline-success" @click="next">
                            {{GetNextTitle}}
                        </b-button>
                    </div>
                </div>
                <div v-else-if="this.type === 'news'">
                    <div align="center" style="border-bottom: 2px solid rgba(201,202,202,0.99)">
                        <h2>{{news_GetCurrentTitle}}</h2>
                        <time>{{news_GetCurrentNewsTime}}</time>
                    </div>
                    <div>
                        <p>{{news_GetCurrentContent}}</p>
                    </div>
                    <div>
                        <span>上一条: </span>
                        <b-button :disabled="news_prev_is_disabled" pill variant="outline-success" @click="news_prev">
                            {{news_GetPrevTitle}}
                        </b-button>
                        <br/>
                        <span>下一条: </span>
                        <b-button :disabled="news_next_is_disabled" pill variant="outline-success" @click="news_next">
                            {{news_GetNextTitle}}
                        </b-button>
                    </div>
                </div>
            </div>
        </my_section>
    </div>
</template>

<script>
    import {GetHomeEncyclopedias} from "../network/home_encyclopedias";
    import {GetConsultingNews} from "../network/consulting_news";
    import my_section from "../components/my_section";
    import {backTop} from "../assets/to_top";

    export default {
        name: "news",
        data() {
            return {
                list: [],
                current_index: 0,
                count: 0,

                news: [],
                current_index_news: 0,
                count_news: 0,

                type: "",
            }
        },
        components: {
            my_section,
        },
        methods: {
            news_prev() {
               if (this.current_index_news > 0){
                   this.current_index_news = this.current_index_news - 1;
               }
            },
            news_next() {
                if (this.current_index_news < this.count_news - 1) {
                    this.current_index_news = this.current_index_news + 1;
                }
            },
            prev() {
                if (this.current_index > 0) {
                    this.current_index = this.current_index - 1;
                }
            },
            next() {
                if (this.current_index < this.count - 1) {
                    this.current_index = this.current_index + 1;
                }
            }
        },
        computed: {
            news_prev_is_disabled(){
                if (this.current_index_news == 0){
                    return true;
                }
                else{
                    return false;
                }
            },
            prev_is_disabled() {
                if (this.current_index == 0) {
                    return true;
                } else {
                    return false;
                }

            },
            news_next_is_disabled(){
                if (this.current_index_news == this.count_news - 1){
                    return true;
                }
                else{
                    return false;
                }
            },
            next_is_disabled() {
                if (this.current_index == this.count - 1) {
                    return true;
                } else {
                    return false;
                }
            },
            news_GetPrevTitle(){
                if (this.news && this.current_index_news < this.count_news && this.news[this.current_index_news]) {
                    if (this.news_prev_is_disabled) {
                        return "到底了~"
                    } else {
                        return this.news[this.current_index_news - 1].title
                    }
                } else {
                    return "到底了~";
                }
            } ,
            GetPrevTitle() {
                if (this.list && this.current_index < this.count && this.list[this.current_index]) {
                    if (this.prev_is_disabled) {
                        return "到底了~"
                    } else {
                        return this.list[this.current_index - 1].problem
                    }
                } else {
                    return "到底了~";
                }
            },
            news_GetNextTitle(){
                if (this.news && this.current_index_news < this.count_news && this.news[this.current_index_news]) {
                    if (this.news_next_is_disabled) {
                        return "到底了~"
                    } else {
                        return this.news[this.current_index_news + 1].title
                    }
                } else {
                    return "到底了~";
                }
            },
            GetNextTitle() {
                if (this.list && this.current_index < this.count && this.list[this.current_index]) {
                    if (this.next_is_disabled) {
                        return "到底了~";
                    } else {
                        return this.list[this.current_index + 1].problem
                    }
                } else {
                    return "到底了~";
                }
            },
            news_GetCurrentTitle(){
                if (this.news && this.current_index_news < this.count_news && this.news[this.current_index_news]) {
                    return this.news[this.current_index_news].title
                } else {
                    return "";
                }
            },
            news_GetCurrentContent(){
                if (this.news && this.current_index_news < this.count_news && this.news[this.current_index_news]) {
                    return this.news[this.current_index_news].content
                } else {
                    return "";
                }
            },
            news_GetCurrentNewsTime() {
                if (this.news && this.current_index_news < this.count_news && this.news[this.current_index_news]) {
                    const time = this.news[this.current_index_news].release_time;
                    const result = time.match("([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9]{2}:[0-9]{2}):.*")
                    return result[1] + " " + result[2];
                } else {
                    return "";
                }
            },
            GetCurrentTitle() {
                if (this.list && this.current_index < this.count && this.list[this.current_index]) {
                    return this.list[this.current_index].problem;
                } else {
                    return "";
                }
            },
            GetCurrentContent() {
                if (this.list && this.current_index < this.count && this.list[this.current_index]) {
                    return this.list[this.current_index].answer;
                } else {
                    return "";
                }
            },
            GetCurrentNewsTime() {
                if (this.list && this.current_index < this.count && this.list[this.current_index]) {
                    const time = this.list[this.current_index].create_time;
                    const result = time.match("([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9]{2}:[0-9]{2}):.*")
                    return result[1] + " " + result[2];
                } else {
                    return "";
                }
            }
        },
        created() {
            this.$http.all([GetHomeEncyclopedias(), GetConsultingNews()]).then(
                this.$http.spread((homes, news) => {
                    this.list = homes.data.results;
                    this.count = homes.data.count;
                    this.news = news.data.results;
                    this.count_news = news.data.count;
                })
            ).catch(error => {
                console.log(error);
            })
        },
        mounted() {
            backTop();
            const temp = [
                {"url": "home", "content": "居家百科", "isActive": true},
                {"url": "news", "content": "最新动态", "isActive": false},
            ]
            this.$store.commit("ChangeEnglishTitle", "NEWS");
            this.$store.commit("ChangeTitle", "咨询动态");
            this.$store.commit("ChangeList", temp);
        },
        beforeUpdate() {
            for (const item of this.$store.getters.GetList) {
                if (item.isActive) {
                    switch (item.url) {
                        case "home":
                            this.type = "home";
                            break;
                        case "news":
                            this.type = "news";
                            break;
                    }
                }
            }
        }
    }
</script>

<style scoped>
    span {
        font-weight: bold;
    }
</style>