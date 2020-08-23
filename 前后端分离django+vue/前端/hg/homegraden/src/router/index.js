import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [

    {
      name: "test",
      path: "/test",
      component: () => import("../components/test")
    },
    {
      path: "/",
      component: () => import("../views/home"),
      children: [
        {
          path: "contact_us/",
          name: "contact_us",
          component: () => import("../views/contact_us"),

        },
        {
          path: "/",
          name: "index",
          component: () => import("../views/index")
        },
        {
          path: "about_us/",
          name: "about_us",
          component: () => import("../views/about_us")
        },
        {
          path: "news/",
          name: "news",
          component: () => import("../views/news")
        },
        {
          path: "customer_cases/",
          name: "customer_cases",
          component: () => import("../views/customer_cases"),
          // children: [
          //   {
          //     path: "detail/:num",
          //     name: "customer_cases_detail",
          //     component: () => import("../views/customer_cases_detail")
          //   }
          // ]
        },
        {
          path: "product_center/",
          name: "product_center",
          component: () => import("../views/product_center"),
          children:[
            {
              path: "detail/:num",
              name: "product_detail",
              component: () => import("../views/product_detail"),
            }
          ]
        }
      ]
    },
]

const router = new VueRouter({
  mode: "history",
  routes
})

export default router
