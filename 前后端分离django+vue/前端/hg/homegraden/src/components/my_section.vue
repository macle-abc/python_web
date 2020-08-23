<template>
    <b-container fluid>
        <b-row>
            <b-col cols="3">
                <left_list_view>
                </left_list_view>
            </b-col>
            <b-col cols="9">
                <div>
                    <h3 id="title">{{ this.$store.state.title }}</h3>
                <b-aspect aspect="4:1">
                    <slot name="content"></slot>
                </b-aspect>
                </div>
            </b-col>
        </b-row>
    </b-container>

</template>

<script>
    import left_list_view from "./base/left_list_view";
    export default {
        name: "my_section",
        components: {
            left_list_view
        },
    }
</script>

<style scoped>
#title{
    color: #126c12;
}
</style>