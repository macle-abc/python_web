<template>
    <div id="border">
        <b-carousel
            fade
            controls
            :interval=3000
            indicators
            style="text-shadow: 1px 1px 2px #333;"
        >
<!--            <slot name="default">-->
<!--                <navbar></navbar>-->
<!--            </slot>-->
            <b-carousel-slide
                    class="carousel_my"
                    v-for="eachImg in imgLists"
                    :key="eachImg.src"
                    :img-src="eachImg.src"
                    :img-alt="eachImg.alt"
            >
<!--                <title_head></title_head>-->
            </b-carousel-slide>
        </b-carousel>
    </div>
</template>

<script>
    import title_head from "./title_head";
    import navbar from "./navbar";
    export default {
        name: "carousel",
        components:{
            title_head,
            navbar,
        },
        data(){
            return {
                imgLists: [
                    {
                        src: require("../assets/images/carousel_1.jpg"),
                        alt: "展示图1"
                    },
                    {
                        src: require("../assets/images/carousel_2.jpg"),
                        alt: "展示图2"
                    },
                    {
                        src: require("../assets/images/carousel_3.jpg"),
                        alt: "展示图3"
                    }
                ]
            }
        }
    }
</script>

<style scoped>
    #border{
        border-top: 1px solid rgba(86,87,87,0.99);
        border-bottom: 1px solid rgba(146,147,147,0.99);
    }
    .carousel_my{
        /*width: 20px;*/
        height:600px;
    }
</style>