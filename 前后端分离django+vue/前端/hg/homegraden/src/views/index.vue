<template>
    <div>
<!--            <left_nav :categories="categories"></left_nav>-->
            <cards_show :infos="products_infos" :type="true"><h1 slot="title">产品简介<b-button variant="success" to="/product_center/">更多+</b-button></h1></cards_show>
            <project_profile></project_profile>
            <cards_show :infos="customer_cases" :type="false"><h1 slot="title">模型方案及实体布局<b-button variant="success" to="/customer_cases/">更多+</b-button></h1> </cards_show>
            <list_view :title="'居家百科'" :cards="home_encyclopedias" :this_router="'/news/'">
            </list_view>
            <list_view :title="'最新动态'" :cards="consulting_news" :this_router="'/news/'">
            </list_view>
    </div>
</template>

<script>
    import {backTop} from "../assets/to_top";
    import {GetProductsInfos, GetCategories} from "../network/products";
    import {GetCustomerCases} from "../network/customer_cases";
    import {GetHomeEncyclopedias} from "../network/home_encyclopedias";
    import {GetConsultingNews} from "../network/consulting_news";

    import left_nav from "../components/base/left_nav";
    import cards_show from "../components/base/cards_show";
    import project_profile from "../components/base/project_profile";
    import list_view from "../components/base/list_view";

    export default {
        name: "index",
        data(){
            return {
                // categories: [],
                customer_cases: [],
                home_encyclopedias: [],
                consulting_news: [],
                products_infos: [],
            }
        },
        components: {
            // left_nav,
            cards_show,
            project_profile,
            list_view,
        },
        mounted() {
            backTop();
            this.$http.all(
                [
                    GetProductsInfos(),
                    // GetCategories(),
                    GetCustomerCases(),
                    GetHomeEncyclopedias(),
                    GetConsultingNews(),
                ]
            ).then(
                this.$http.spread((productsInfos, customerCases, homeEncyclopedias, consultingNews) =>
                {
                    this.products_infos = productsInfos.data.results;
                    let temp = customerCases.data.results;
                    for (const item of temp)
                    {
                        this.customer_cases.push( {
                            "url": item.url,
                            "name": item.name,
                            "image": item.title_page,
                        })
                    }
                    // problem answer
                    temp = homeEncyclopedias.data.results;
                    for (const item of temp)
                    {
                        let temp_answer = ""
                        if (item.answer.length > 20){
                            temp_answer = item.answer.substr(0, 20) + "..."
                        }
                        this.home_encyclopedias.push(
                            {
                                "header": {
                                    "content": item.problem,
                                    "icon": "question-circle"
                                },
                                "footer": {
                                    "content": temp_answer,
                                    "icon": "award"
                                }
                            }
                        )
                    }
                    temp = consultingNews.data.results;
                    for (const item of temp)
                    {
                        let temp_content = item.content;
                        if (temp_content.length > 20){
                            temp_content = item.content.substr(0, 20) + "...";
                        }
                        this.consulting_news.push(
                            {
                                "header": {
                                    "content": item.title,
                                    "icon": "chat-dots"
                                },
                                "footer": {
                                    "content": temp_content,
                                    "icon": "book",
                                }
                            }
                        )
                    }

                })
            ).catch(error => {
                console.log(error);
            })
        },
    }
</script>

<style scoped>

</style>