<template>
    <div>
        <div style="display: none">
            {{this.$store.state.list}}
        </div>
<!--        {{this.title}}-->
<!--        {{this.img_src}}-->
<!--        {{this.imgLists}}-->
<!--        {{this.videoCount}}-->
<!--        {{this.videos}}-->
        <my_section>
            <div slot="content">
                <customer_cases_detail :url="url">

                </customer_cases_detail>
<!--                <router-view></router-view>-->
            </div>
        </my_section>
<!--        <my_section>-->
<!--            <div slot="content">-->
<!--                    <b-card  img-top>-->
<!--                        <b-card-title>-->
<!--                            {{title}}-->
<!--                        </b-card-title>-->
<!--                        <b-button-group>-->
<!--                        <b-button variant="info" :href="video" v-for="video, index in videos" :key="video">视频详情{{index + 1}}-->
<!--                        </b-button>-->
<!--                        </b-button-group>-->
<!--                        <b-card-img-lazy :src="img_src">-->
<!--                        </b-card-img-lazy>-->
<!--                        <b-card-body>-->
<!--                        <b-carousel-->
<!--                                fade-->
<!--                                controls-->
<!--                                :interval=3000-->
<!--                                indicators-->
<!--                                img-width="1024"-->
<!--                                img-height="480"-->
<!--                                style="text-shadow: 1px 1px 2px #333;"-->
<!--                        >-->
<!--                            <b-carousel-slide-->
<!--                                    v-for="eachImg in imgLists"-->
<!--                                    :key="eachImg"-->
<!--                                    :img-src="eachImg"-->
<!--                            >-->
<!--                            </b-carousel-slide>-->
<!--                        </b-carousel>-->
<!--                        </b-card-body>-->
<!--                    </b-card>-->


<!--            </div>-->
<!--        </my_section>-->
    </div>
</template>

<script>
    import my_section from "../components/my_section";
    import {backTop} from "../assets/to_top";
    import {GetCustomerCases, GetCustomerCasesImagesDetail, GetVideo} from "../network/customer_cases";
    import customer_cases_detail from "./customer_cases_detail";
    export default {
        name: "customer_cases",
        data(){
            return {
                "url": "",
            }
        },
        components: {
            my_section,
            customer_cases_detail,
        },
        methods: {

        },
        beforeUpdate() {
            for (const item of this.$store.state.list)
            {
                if (item.isActive)
                {
                    // this.title = item.content;
                    // this.img_src = item.title_page;
                    // this.imgLists = item.customer_cases_images;
                    this.url = item.url;
                    break;
                }
            }
        },
        created() {
            GetCustomerCases().then(
                data => {
                    const results = data.data.results;
                    let list = []
                    for (const item of results)
                    {
                        list.push(
                            {
                                "url": item.url,
                                "isActive": false,
                                "content": item.name,
                            }
                        )
                    }
                    if (list.length > 0)
                    {
                        list[0].isActive = true
                    }
                    this.$store.commit("ChangeList", list)
                }
            ).catch(error => {
                console.log(error);
            })
        },
        // created() {
        //     GetCustomerCases().then(
        //         data => {
        //             const results = data.data.results
        //             let list = [];
        //             // this.videoCount = data.data.results.customer_cases_videos.length;
        //             let videosapi = [];
        //             for (const item of data.data.results[0].customer_cases_videos)
        //             {
        //                 videosapi.push(GetVideo(item))
        //             }
        //             this.$http.all(videosapi).then(
        //                 temp_video_data => {
        //                     let temp_videos = [];
        //                     for (const each of temp_video_data)
        //                     {
        //                         console.log(each.data);
        //                         temp_videos.push(each.data.video_effect);
        //                     }
        //                     this.videos = temp_videos;
        //                     this.videoCount = this.videos.length;
        //                 }
        //             ).catch(error => {
        //                 console.log(error);
        //             })
        //
        //             // console.log(this.videos);
        //             // this.videoCount = this.videos.length;
        //             for (const item of results)
        //             {
        //                 let request_images = []
        //                 for (const imgApi of item.customer_cases_images)
        //                 {
        //                     request_images.push(GetCustomerCasesImagesDetail(imgApi))
        //                 }
        //                 let temp_customer_cases_iamges = []
        //                 this.$http.all(request_images).then(
        //                     data => {
        //                         for (const each of data)
        //                         {
        //                             temp_customer_cases_iamges.push(each.data.image);
        //                         }
        //                     }
        //                 ).catch(error => {
        //                     console.log(error);
        //                 })
        //                 list.push(
        //                     {
        //                         'url': item.url,
        //                         "content": item.name,
        //                         "title_page": item.title_page,
        //                         "customer_cases_images": temp_customer_cases_iamges,
        //                         "isActive": false,
        //                     }
        //                 )
        //             }
        //             if (list.length > 0)
        //             {
        //                 list[0].isActive = true;
        //             }
        //
        //            this.$store.commit("ChangeList", list);
        //         }
        //     ).catch(error => {
        //         console.log(error);
        //     })
        // },
        mounted() {
            backTop();
            this.$store.commit("ChangeEnglishTitle", "MODEL SOLUTIONS AND ENTITIES LAYOUT");
            this.$store.commit("ChangeTitle", "模型方案及实体布局");
        }
    }
</script>

<style scoped>

</style>