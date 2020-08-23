<template>
    <div>
        <b-nav vertical>
            <b-nav-dropdown text="产品分类" lazy>
                <b-nav-item v-for="category in categories" :key="category.url">
                    {{ category.classification }}

<!--                    路由跳转功能：-->
                </b-nav-item>
            </b-nav-dropdown>
        </b-nav>
    </div>
</template>

<script>
    export default {
        name: "left_nav",
        props: {
            categories: {
                type: Array,
                required: true,
            }
        }
    }
</script>

<style scoped>

</style>