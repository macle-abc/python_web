from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import HomeEncyclopediasListView, HomeEncyclopediasDetailView

urlpatterns = [
    path('home_encyclopedias/', HomeEncyclopediasListView.as_view(), name="home_encyclopedias-list"),
    path('home_encyclopedias/<int:pk>', HomeEncyclopediasDetailView.as_view(), name="home_encyclopedias-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
