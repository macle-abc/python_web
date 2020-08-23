<template>
   <div>
<!--      关于我们-->
<!--       小标题-->
<!--      项目名 -->
<!--详情-->
<!--       跳转关于我们-->
<!--       图片-->
      <b-card border-variant="success">
          <b-card-title title="关于我们"></b-card-title>
          <b-card-sub-title
                  sub-title="个性化设计 绿化装饰 居家小空间"
                  sub-title-text-variant="info"
          ></b-card-sub-title>
          <b-card-header
                  header-border-variant="success"
                  header-text-variant="dark"
          >家庭花园</b-card-header>
          <b-card-body
            body-text-variant="dark"
          >
              将建筑设计与园林设计相结合根据消费者家中的阳台类型及日照、通风条件对业主家中的庭院、阳台、墙壁进行有设计性的绿化布置丰富人们的生活情趣，改善居住环境在净化空气的同时，为家居风格起到画龙点睛的作用，观赏性极佳。
              <b-button to="/about_us/" variant="outline-success">
                  关于我们
              </b-button>
          </b-card-body>
      </b-card>
   </div>
</template>

<script>
    export default {
        name: "team_profile"
    }
</script>

<style scoped>

</style>