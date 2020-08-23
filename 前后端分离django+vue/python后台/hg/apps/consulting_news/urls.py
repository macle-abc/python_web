from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from .views import ConsultingNewsDetail, ConsultingNewsList

urlpatterns = format_suffix_patterns([
    path('consulting_news/', ConsultingNewsList.as_view(), name="consulting_news-list"),
    path("consulting_news/<int:pk>/", ConsultingNewsDetail.as_view(), name="consulting_news-detail"),
])