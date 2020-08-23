<template>
    <div>
        <!--        <div style="display: none">-->
        <!--           {{this.$store.state.list}}-->
        <!--        </div>-->
        <!--        {{this.url}}-->
        <!--        <my_section>-->
        <!--            <div slot="content">-->
        <b-card img-top>
            <b-card-title>
                {{title}}
            </b-card-title>
            <b-button-group>
                <b-button variant="info" :href="video" v-for="video, index in videos" :key="video">视频详情{{index + 1}}
                </b-button>
            </b-button-group>
            <!--                    <b-card-img-lazy :src="img_src">-->
            <!--                    </b-card-img-lazy>-->
            <b-card-body>
                <b-carousel
                        fade
                        controls
                        :interval=3000
                        indicators
                        img-width="1024"
                        img-height="480"
                        style="text-shadow: 1px 1px 2px #333;"
                >
                    <b-carousel-slide
                            v-for="eachImg in imgLists"
                            :key="eachImg"
                            :img-src="eachImg"
                            img-height="480"
                    >
                    </b-carousel-slide>
                </b-carousel>
            </b-card-body>
        </b-card>


    </div>
    <!--        </my_section>-->
    <!--    </div>-->
</template>

<script>

    import {GetCustomerCasesImagesDetail} from "../network/customer_cases";

    export default {
        name: "customer_cases_detail",
        data() {
            return {
                "title": "",
                "imgLists": "",
                "videos": "",
            }
        },
        props: {
            url: {
                type: String,
                required: true,
            }
        },
        watch: {
            url: function (newValue, oldValue) {
                console.log(newValue);
                GetCustomerCasesImagesDetail(newValue).then(
                    data => {
                        const results = data.data
                        this.title = results.name
                        let imgs = []
                        let videos = []
                        for (const item of results.customer_cases_images) {
                            imgs.push(GetCustomerCasesImagesDetail(item))
                        }
                        for (const item of results.customer_cases_videos) {
                            videos.push(GetCustomerCasesImagesDetail(item))
                        }
                        this.$http.all(imgs).then(
                            data => {
                                let images = []
                                for (const item of data) {
                                    images.push(item.data.image);
                                }
                                this.imgLists = images
                            }
                        ).catch(error => {
                            console.log(error);
                        })
                        this.$http.all(videos).then(
                            data => {
                                let videos = []
                                for (const item of data){
                                    videos.push(item.data.video_effect);
                                }
                                this.videos = videos
                                // console.log(data, "99");
                            }
                        ).catch(error => {
                            console.log(error);
                        })
                    }
                ).catch(error => {
                    console.log(error);
                })
            }
        }
    }
    // created() {
    //     console.log("created");
    // },
    // mounted() {
    //     console.log("mounted");
    // }
    // activated() {
    //     console.log("activated");
    // }
    //     beforeUpdate() {

    // }
</script>

<style scoped>
</style>