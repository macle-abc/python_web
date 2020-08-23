<template>
    <div>
        <b-card align="center">
            <div id="text">
            <b-card-title style="font-size: 50px; color: rgba(88,124,36,0.99); padding-bottom: 20px">
                {{product_info.name}}
            </b-card-title>
            <b-card-sub-title sub-title-text-variant="info" style="font-size:40px; padding-bottom: 20px">
                {{product_info.style}}
            </b-card-sub-title>
            <b-card-text style="border-bottom: 2px solid">
                地点:
                {{product_info.site}}
            </b-card-text>
            <b-card-text>
                {{product_info.key_word}}
            </b-card-text>
            <b-card-text style="color: rgba(163,164,164,0.99); font-size: 20px">
                {{product_info.feature}}
            </b-card-text>
            </div>
            <div id="image">
            <b-img-lazy v-for="image in images" :src="image" :key="image" thumbnail width="400">
            </b-img-lazy>
            </div>
        </b-card>
    </div>
</template>

<script>
    import {GetProductDetail} from "../network/products";

    export default {
        name: "product_detail",
        data() {
            return {
                product_info: {},
                images: [],
            }
        },

        watch: {
            '$route.path': function (newVal, oldVal) {
                GetProductDetail("https://api.akmduj.cn/products/" + this.$route.params.num).then(data => {
                    this.product_info = data.data
                    let imageApi = [];
                    for (const item of data.data.products_images) {
                        imageApi.push(GetProductDetail(item))
                    }
                    this.$http.all(imageApi).then(
                        data => {
                            let images = []
                            for (const item of data) {
                                images.push(item.data.image)
                                // this.images.push()
                            }
                            this.images = images;
                        }
                    ).catch(error => {
                        console.log(error);
                    })
                }).catch(error => {
                    console.log(error);
                })
            }
        },
        mounted() {
            GetProductDetail("https://api.akmduj.cn/products/" + this.$route.params.num).then(data => {
                this.product_info = data.data
                let imageApi = [];
                for (const item of data.data.products_images)
                {
                    imageApi.push(GetProductDetail(item))
                }
                this.$http.all(imageApi).then(
                    data => {
                        let images = []
                        for (const item of data)
                        {
                            images.push(item.data.image)
                            // this.images.push()
                        }
                        this.images = images;
                    }
                ).catch(error => {
                    console.log(error);
                })
            }).catch(error => {
                console.log(error);
            })
        }
    }
</script>

<style scoped>
#image{
    border: 2px solid rgba(202,172,98,0.99) ;
}
#text{
        font-size: 30px;
    /*color: rgba(163,164,164,0.99);*/
    /*color: rgba(202,188,128,0.99)*/
    color: rgba(124,113,73,0.99);
 /*font-family: Microsoft YaHei,'宋体' , Tahoma, Helvetica, Arial, "\5b8b\4f53", sans-serif;*/
    }
</style>