​
<template>
    <div>
        <b-avatar button @click="goTop" v-show="goTopShow" class="goTop">
            <b-icon-chevron-double-up variant="info"></b-icon-chevron-double-up>
        </b-avatar>
    </div>
</template>
<script>
    export default {
        name: "backup",
        data() {
            return {
                scrollTop: "",
                goTopShow: false
            };
        },
        watch: {
            scrollTop(val) {
                if (this.scrollTop > 500) {
                    this.goTopShow = true;
                } else {
                    this.goTopShow = false;
                }
            }
        },
        methods: {
            handleScroll() {
                this.scrollTop =
                    window.pageYOffset ||
                    document.documentElement.scrollTop ||
                    document.body.scrollTop;
                if (this.scrollTop > 500) {
                    this.goTopShow = true;
                }
            },
            goTop() {
                let timer = null,
                    _that = this;
                cancelAnimationFrame(timer);
                timer = requestAnimationFrame(function fn() {
                    if (_that.scrollTop > 0) {
                        _that.scrollTop -= 50;
                        document.body.scrollTop = document.documentElement.scrollTop =
                            _that.scrollTop;
                        timer = requestAnimationFrame(fn);
                    } else {
                        cancelAnimationFrame(timer);
                        _that.goTopShow = false;
                    }
                });
            }
        },
        mounted() {
            window.addEventListener("scroll", this.handleScroll);
        },
        destroyed() {
            window.removeEventListener("scroll", this.handleScroll);
        }
    };
</script>

<style scoped>
    .goTop {
        position: fixed;
        right: 40px;
        bottom: 60px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #fff;
        padding: 10px;
        cursor: pointer;
        box-shadow: 0 0 6px rgba(0, 0, 0, 0.12);
        z-index: 2;
    }
</style>

​