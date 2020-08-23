<template>
   <div>
       <b-jumbotron fluid bg-variant="success" border-variant="dark">
           <b-container fluid>
               <b-row>
                   <b-col class="content" id="first">
                       <div>
                           <h1>家庭花园</h1>
                            <p>家庭花园是一个主营绿化设计，兼营售卖、养护、后期指导为一体，专注于家庭细部花卉装饰的全新服务。</p>
                       </div>
                   </b-col>
                   <b-col class="content">
                       <div>
                           最新推文
                           <b-nav vertical>
                               <b-nav-item v-for="url in urls" :key="url.url"
                                           link-classes="my_nav_item"
                                           :href="url.url"
                                           >
                                    {{ url.title }}
                               </b-nav-item>
                           </b-nav>
                       </div>
                   </b-col>
                   <b-col class="content">
                       <div>
                           快速链接
                           <b-nav vertical>
                               <b-nav-item to="/product_center/" link-classes="my_nav_item">
                                   产品中心
                               </b-nav-item>
                               <b-nav-item to="/customer_cases/" link-classes="my_nav_item">
                                   模型方案及实体布局
                               </b-nav-item>
                               <b-nav-item to="/news/" link-classes="my_nav_item">
                                   咨询动态
                               </b-nav-item>
                               <b-nav-item to="/about_us/" link-classes="my_nav_item">
                                   关于我们
                               </b-nav-item>
                           </b-nav>
                       </div>
                   </b-col>
                   <b-col class="content">
                       <div>
                           <p>联系我们</p>
                           <b-list-group flush>
                               <b-list-group-item variant="light">
                                   <b-icon-phone></b-icon-phone>
                                   150****2375
                               </b-list-group-item>
                               <b-list-group-item variant="light">
<!--                                   <b-icon-chat-dots-fill variant="success">-->
<!--                                   </b-icon-chat-dots-fill>-->
                                   <b-img
                                           fluid
                                           width="200"
                                           height="150"
                                           :src="require('../assets/images/scan.png')">

                                   </b-img>
<!--                                   家庭花园-->
                               </b-list-group-item>
                               <b-list-group-item variant="light">
                                   <b-icon-envelope></b-icon-envelope>
                                    176****247@qq.com
                               </b-list-group-item>
                           </b-list-group>
                       </div>
                   </b-col>
               </b-row>
           </b-container>

       </b-jumbotron>
   </div>
</template>

<script>
    export default {
        name: "my_footer",
        data(){
            return {
                urls: [
                    {
                        "url": "https://mp.weixin.qq.com/s?__biz=MzI2NDYxNjM5NQ==&mid=2247483715&idx=1&sn=6b224bbbeae24f221e08f2f86a6304e5&chksm=eaa8a1e7dddf28f1a96710a8c4a27ae4b3e23869f5bf8ba6aa1bd2f920ed1cee27711e6081a9&token=2141607545&lang=zh_CN#rd",
                        "title": "季节循环，顺时而生深，应运而为"
                    },
                    {
                        "url": "https://mp.weixin.qq.com/s?__biz=MzI2NDYxNjM5NQ==&mid=2247483677&idx=1&sn=18983976f3cb67b2b9e922a7629c5431&chksm=eaa8a1b9dddf28af7e48e543c894b9553915a51c42adbef0f3da99633ea31dfc3659131a8175&token=2141607545&lang=zh_CN#rd",
                        "title": "你是“绿手指”吗？在家也想感受大自然？六个步骤打造完美家庭花园！"
                    },
                    {
                        "url": "https://mp.weixin.qq.com/s?__biz=MzI2NDYxNjM5NQ==&mid=2247483655&idx=1&sn=bb6cdf0be8ea9e9da3ffe9eb38a7e312&chksm=eaa8a1a3dddf28b56db76c34c2eaaee23cbd217b1152844ccedb668160686c8e29c52f340ac3&token=2141607545&lang=zh_CN#rd",
                        "title": "贴近自然，尽享生活——你的家庭花园"
                    }
                ]
            }
        }
    }
</script>

<style scoped>
    .content{
        color: white;
        border-left: 1px solid rgba(201, 202, 202, 0.7);
    }
    #first{
        border-left: none;
    }

    .my_nav_item{
        color: rgba(231,255,187,0.83);

    }
    .my_nav_item:hover{
        /*color: rgba(202, 172, 98, 0.99);*/
        text-decoration: underline;
    }
</style>