<template>
    <div>
        <navbar :products_infos="products_infos"></navbar>
        <carousel></carousel>
        <router-view></router-view>
        <my_footer></my_footer>
        <backup></backup>
    </div>
</template>

<script>
    import {GetProductsInfos} from "../network/products";
    import {backTop} from "../assets/to_top";

    import backup from "../components/backup";
    import carousel from "../components/carousel";
    import navbar from "../components/navbar";
    import my_footer from "../components/my_footer";

    export default {
        name: "home",
        components: {
            carousel,
            navbar,
            my_footer,
            backup,
        },
        data() {
            return {
                products_infos: [],
            }
        },
        mounted() {
            backTop();
            GetProductsInfos().then(data => {
                this.products_infos = data.data.results;
            }).catch(error => {
                console.log(error);
            })
        }

    }
</script>

<style scoped>

</style>