<template>
    <div>
        <b-card no-body>
            <b-card-title>
                <p id="english_title">{{ this.$store.state.englishTitle }}</p>
                <p id="title">{{ this.$store.state.title }}</p>
            </b-card-title>
            <b-list-group flush>
                <b-list-group-item button v-for="item in this.$store.state.list"
                                   :key="item.url" :active="item.isActive" variant="info" @click="click(item)">
                    <b-container fluid>
                        <b-row>
                           <b-col cols="1">
                               <b-icon-dot></b-icon-dot>
                           </b-col>
                            <b-col cols="8">
                                {{ item.content }}
                            </b-col>
                            <b-col>
                                <b-icon-chevron-double-right></b-icon-chevron-double-right>
                            </b-col>
                        </b-row>

                    </b-container>
                </b-list-group-item>
            </b-list-group>
        </b-card>
    </div>
</template>

<script>
    export default {
        name: "left_list_view",
        methods: {
            click(which){
                this.$store.commit("WhoClick", which);
            }
        }
    }
</script>

<style scoped>
#english_title{
    color: #126c12;
}
    #title{
        /*color: #28a745;*/
    }
</style>