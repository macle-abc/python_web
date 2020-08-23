<template>
    <div>
        <slot name="title"></slot>
        <b-card-group deck>

            <b-card
                border-variant="success"
                body-text-variant="success"
                align="center"
                v-for="info in infos"
                :key="info.url"
                :img-src="info.cover"
            >
                <template v-if="type === false">
                    <b-card-title align="left">{{info.name}}</b-card-title>
                </template>
                <template v-else>
                    <b-card-title>{{info.name}}</b-card-title>
                    <b-button variant="info" :to="changeUrl(info.url)">详情</b-button>
                </template>
            </b-card>
        </b-card-group>
    </div>
</template>

<script>
    export default {
        name: "cards_show",
        props: {
            infos: {
                type: Array,
                required: true
            },
            type: {
                type: Boolean,
                required: true,
            }
        },
        methods: {
            changeUrl(url){
                    return "/product_center/detail/" + url.substr("https://api.akmduj.cn/products/".length);
            }
        }
    }
</script>

<style scoped>

</style>