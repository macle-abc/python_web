<template>
    <div>
        <b-navbar toggleable="xl" type="dark" variant="dark" sticky>
            <b-navbar-brand to="/">
                <b-avatar :src="require('../assets/images/logo.png')" square></b-avatar>
                <b-icon-house-fill variant="success"></b-icon-house-fill>
                首页
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav align="center">

<!--                </b-navbar-nav>-->
<!--                <b-navbar-nav align="center">-->
                    <b-nav-item to="/customer_cases/">
                        模型方案及实体布局
                    </b-nav-item>

                    <b-nav-item to="/news/">
                        咨询动态
                    </b-nav-item>


                    <b-nav-item to="/contact_us/">
                        联系我们
                    </b-nav-item>
                    <b-nav-item to="/about_us/">
                        关于我们
                    </b-nav-item>
                    <b-nav-item-dropdown text="产品中心" right no-flip dropright>
                        <b-dropdown-item v-for="products_info in products_infos"
                                         :key="products_info.url" :to="changeToProduct(products_info.url)"
                        >
                            {{products_info.name}}
                        </b-dropdown-item>
                        <b-dropdown-divider>
                        </b-dropdown-divider>
                        <b-dropdown-item to="/product_center/">
                            更多+
                        </b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>

<!--                <b-navbar-nav class="ml-auto" align="center">-->
<!--                    <b-nav-form>-->
<!--                        <b-form-input size="sm" class="mr-sm-2" placeholder="搜索"></b-form-input>-->
<!--                        <b-button size="sm" class="my-2 my-sm-0" type="submit" variant="outline-success">-->
<!--                            <b-icon-search></b-icon-search></b-button>-->
<!--                    </b-nav-form>-->
<!--                </b-navbar-nav>-->
            </b-collapse>
        </b-navbar>

    </div>
</template>

<script>
    export default {
        name: "navbar",
        props: {
            products_infos: {
                type: Array,
                required: true,
            }
        },
        methods:{
            changeToProduct(url){
                return "/product_center/detail/" + url.substr("https://api.akmduj.cn/products/".length);
            }
        }
    }
</script>

<style scoped>

</style>