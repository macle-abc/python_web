<template>
    <div>
        <div id="no">
            {{listData}}
        </div>
        <my_section>
            <div slot="content">
                <div v-if='this.type === "person"'>
                    <b-card-group>
                        <b-card v-for="person_info in person_infos" :key="person_info.phone">
                            <b-card-img-lazy :src="person_info.img_src">
                            </b-card-img-lazy>
                            <b-card-body>
                                <b-card-title>
                                    {{person_info.occupation}}
                                </b-card-title>
                                <b-card-text>
                                    {{person_info.name}}
                                </b-card-text>
                                <b-card-text>
                                    <b-icon-phone variant="info">
                                    </b-icon-phone>
                                    {{person_info.phone}}
                                </b-card-text>
                                <b-card-text>
                                <b-icon-envelope variant="info">
                                </b-icon-envelope>
                                    {{person_info.email}}
                                </b-card-text>
                            </b-card-body>
                        </b-card>
                    </b-card-group>
<!--                    人员-->
                </div>
                <div v-else-if='this.type === "team"'>
                    <p>
                        本项目的管理团队由江西科技师范大学的王小雨、张芳、罗理民、刘月琼四名学生组成。凭借人员储备的多样性，我们在设计、技术、资金方面都有极大的优势。团队成员具备出色的管理能力、设计能力、专业的知识储备、资金的掌控能力、计算机知识的掌握、网站开发的能力，且团队成员具有积极进取的精神和优越的创新能力。
                    </p>
<!--                    团队-->
                </div>
            </div>
        </my_section>
    </div>
</template>

<script>
    import {backTop} from "../assets/to_top";
    import my_section from "../components/my_section";

    export default {
        name: "about_us",
        components: {
            my_section,
        },
        data() {
            return {
                type: "",
                person_infos: [
                    {
                        "img_src": require("../assets/images/team/wxy.jpg"),
                        "name": "王小雨",
                        "phone": "150****2375",
                        "email": "176****247@qq.com",
                        "occupation": "执行董事"
                    },
                    {
                        "img_src": require("../assets/images/team/zf.jpg"),
                        "name": "张芳",
                        "phone": "155****6573",
                        "email": "302****059@qq.com",
                        "occupation": "市场总监"
                    },
                    {
                        "img_src": require("../assets/images/team/llm.jpg"),
                        "name": "罗理民",
                        "phone": "187****7152",
                        "email": "333****975@qq.com",
                        "occupation": "财务总监"
                    },
                    {
                       "img_src": require("../assets/images/team/lyq.jpg"),
                       "name": "刘月琼",
                       "phone": "130****9959",
                       "email": "203****268@qq.com",
                        "occupation": "运营总监",
                    },
                ]
            }
        },
        computed: {
            listData() {
                return this.$store.state.list;
            }
        },
        mounted() {
            const list = [
                {"url": "team", "content": "团队简介", "isActive": true},
                {"url": "person", "content": "人员介绍", "isActive": false},
            ]
            backTop();
            this.$store.commit("ChangeEnglishTitle", "ABOUT US");
            this.$store.commit("ChangeTitle", "关于我们");
            this.$store.commit("ChangeList", list);
        },
        beforeUpdate() {
            for (const item of this.$store.getters.GetList) {
                if (item.isActive) {
                    switch (item.url) {
                        case "team":
                            this.type = "team";
                            break;
                        case "person":
                            this.type = "person";
                            break;
                    }
                }
            }
        },
    }
</script>

<style scoped>
    #no {
        display: none;
    }
</style>