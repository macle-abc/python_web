<template>
    <div>
        <template v-if="this.$route.path !== '/product_center/'">
<!--            <product_detail :url="url"></product_detail>-->
            <router-view></router-view>
        </template>
        <template v-else>
            <my_section>
                <div slot="content">
                    <b-card-group>
                        <b-card v-for="product in products" :key="product.url">
<!--                            {{product}}-->
                            <b-card-title>
                                {{product.name}}
                            </b-card-title>
                            <b-card-img-lazy :src="product.cover">
                            </b-card-img-lazy>
                            <b-button variant="success" :to="detail(product.url)">产品详情</b-button>
                        </b-card>
                    </b-card-group>
                </div>
            </my_section>
        </template>
    </div>
</template>

<script>
    import product_detail from "./product_detail";
    import {backTop} from "../assets/to_top";
    import my_section from "../components/my_section";
    import {GetCategories, GetProductsInfos, GetProductsByCategories} from "../network/products";

    export default {
        name: "product_center",
        data() {
            return {
                products: [],
                count: [],
            }
        },
        methods: {
            detail(url){
                return "/product_center/detail/" + url.substr("https://api.akmduj.cn/products/".length);
            }
        },
        components: {
            my_section,
            product_detail,
        },
        created() {
            GetProductsInfos().then(data => {
                this.products = data.data.results
                this.count = data.data.length
                // for (const item of products.kk)
                // this.$http.get()
            })
        },
        mounted() {
            backTop();
            this.$store.commit("ChangeEnglishTitle", "PRODUCT CENTER")
            this.$store.commit("ChangeTitle", "产品中心")
            this.$store.commit("ChangeList", [{"url": "product", "content": "产品中心", "isActive": true}])
        }
    }
        // created() {
            // this.$http.all([GetCategories(), GetProductsInfos()]).then(
            //     data => {
            //         this.productsInfos = data[1].data;
            //         let categories_request = [];
            //         for (const item of data[0].data)
            //         {
            //             let temp = [];
            //             GetProductsByCategories(item.url).then(data => {
            //                 temp = data.data;
            //                 categories_request.push({
            //                     "classification": item.classification,
            //                     "products": temp,
            //                 })
            //             }).catch(error => {
            //                 console.log(error);})
            //         }
            //         this.categories_info = categories_request
            //         console.log(typeof categories_request, categories_request, 47, categories_request.length, [1, 2].length);
            //         this.count = categories_request.length
                // }
            // ).catch(error => {
            //     console.log(error);
            // })
        // },
        //
        // mounted() {
        //     backTop();
        //     console.log(this.categories_info);
        //     console.log(this.productsInfos);
        // },
        // updated() {
        //     let temp = [];
        //     for (const item of this.categories_info)
        //     {
        //         temp.push(
        //             {
        //                 "url": item.classfication,
        //                 "content": item.classfication,
        //                 "isActive": false,
        //             }
        //         )
        //     }
        //     {
        //         console.log(this.count);
        //         console.log(temp);
        //         this.$store.commit("ChangeEnglishTitle", "PRODUCT CENTER");
        //         this.$store.commit("ChangeTitle", "产品中心");
        //         this.$store.commit("ChangeList", temp);
        //     }
        //     console.log(temp);

            // console.log(this.categories_info);
        // }
</script>

<style scoped>

</style>