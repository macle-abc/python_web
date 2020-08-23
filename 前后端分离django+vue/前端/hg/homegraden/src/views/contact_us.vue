<template>
    <div>
        <my_section>
            <div slot="content">
                <b-card border-variant="success" align="center">
                    <b-card-text>
                        <b-icon-map variant="info">
                        </b-icon-map>
                        江西省南昌市昌北经济开发区枫林大道605号
                    </b-card-text>
                    <b-card-text>
                        <b-icon-phone variant="info"></b-icon-phone>
                        150****2375

                        <b-icon-phone variant="info"></b-icon-phone>
                        155****6573

                        <b-icon-phone variant="info"></b-icon-phone>
                        187****7152

                        <b-icon-phone variant="info"></b-icon-phone>
                        130****9959
                    </b-card-text>
                    <b-card-text>
                        <b-icon-envelope variant="info"></b-icon-envelope>
                        176****247@qq.com

                        <b-icon-envelope variant="info"></b-icon-envelope>
                        302****059@qq.com

                        <b-icon-envelope variant="info"></b-icon-envelope>
                        333****975@qq.com

                        <b-icon-envelope variant="info"></b-icon-envelope>
                        203****268@qq.com
                    </b-card-text>
                </b-card>
            </div>
        </my_section>
    </div>
</template>

<script>
    import my_section from "../components/my_section";
    import {backTop} from "../assets/to_top";

    export default {
        name: "contact_us",
        components:{
            my_section,
        },
        mounted() {
            backTop();
            const temp = [
                {"url": "contact_use", "content": "联系我们", "isActive": true}
            ]
            this.$store.commit("ChangeEnglishTitle", "CONTACT US");
            this.$store.commit("ChangeTitle", "联系我们");
            this.$store.commit("ChangeList", temp);
        }
    }
</script>

<style scoped>

</style>