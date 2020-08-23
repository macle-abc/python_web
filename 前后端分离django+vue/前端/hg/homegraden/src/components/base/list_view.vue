<template>
    <div>
<!--    <h1>居家百科<b-button variant="outline-primary"><b-icon-chevron-double-right></b-icon-chevron-double-right></b-button></h1>-->
        <h1>
            {{ title }}
            <b-button :to="this_router" variant="success">
            <b-icon-chevron-double-right></b-icon-chevron-double-right>
            </b-button>
        </h1>
    <b-card-group>
        <b-card v-for="card in cards" :key="card.header.content">
            <b-card-header>
                <b-icon :icon="card.header.icon"></b-icon>
                &nbsp;

                &nbsp;
                <span>{{ card.header.content }}</span>
            </b-card-header>
            <b-card-footer>
                <b-icon :icon="card.footer.icon"></b-icon>

                &nbsp;
                &nbsp;
                <span>{{ card.footer.content }}</span>
            </b-card-footer>
        </b-card>
    </b-card-group>
    </div>
</template>

<script>
    export default {
        name: "temp",
        props: {
            title: {
                type: String,
                required: true,
            },
            cards: {
                type: Array,
                required: true,
            },
            this_router: {
                type:String,
                required: true,
            }
        }
    }
</script>

<style scoped>

</style>