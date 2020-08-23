from django.urls import path

from .views import *

urlpatterns = [
    path('test/', test.as_view(), name="test"),

    path('login/', Login.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),

    path('rental/<int:page>', UserRentalView.as_view(), name="rental"),

    path('index/', Index.as_view(), name="index"),
    path('forgot/', ForGot.as_view(), name="forgot"),
    path('about/', About.as_view(), name="about"),
    # path('shop/<path:category>', Shop.as_view(), name="shop"),

    path('shop/', Shop.as_view(), name="shop"),  # 默认显示全部

    path('shop/categories/<path:category>', Shop.as_view(), name="shop_categories"),  # 根据图书分类过滤  get请求

    # path('shop/author/', Shop.as_view(), name="shop_author"),  # 根据作者过滤 post请求 redirect到get请求
    path('shop/author/<path:author>', Shop.as_view(), name="shop_author_get"),

    # path('shop/added_time/', Shop.as_view(), name="shop_added_time"), # 根据时间过滤 post请求 redirect到get请求
    path('shop/added_time/<path:added_time>', Shop.as_view(), name="shop_added_time_get"),

    path('shop/recommend/<int:recommend>', Shop.as_view(), name="shop_recommend"), # 根据喜欢程度过滤 get请求

    path('thumbs/<path:ISBN>', Thumbs.as_view(), name="thumbs"),  # 处理点赞功能

    path('checkout/', Checkout.as_view(), name="checkout"),
    path('search/', Search.as_view(), name="search"), # redirect到shop中

    path('contact/', Contact.as_view(), name="contact"),
    path('single_product/<path:ISBN>', SingleProduct.as_view(), name="single_product"),
    path('wish/', Wish.as_view(), name="wish"),
    path('suggest/', Suggest.as_view(), name="suggest"),

    path('process/<path:account>', Process.as_view(), name="process"),
    path('delete/<path:ISBN>', Delete.as_view(), name="delete"),
]
