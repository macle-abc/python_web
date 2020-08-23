from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CustomerCasesImagesListView, CustomerCasesListView, CustomerCasesDetailView, \
    CustomerCasesImagesDetailView, CustomerCasesVideosListView, CustomerCasesVideosDetailView

urlpatterns = [
    path("customer_cases/", CustomerCasesListView.as_view(), name="customer_cases-list"),
    path("customer_cases/<int:pk>/", CustomerCasesDetailView.as_view(), name="customer_cases-detail"),
    path("customer_cases_images/", CustomerCasesImagesListView.as_view(), name="customer_cases_images-list"),
    path("customer_cases_images/<int:pk>/", CustomerCasesImagesDetailView.as_view(),
         name="customer_cases_images-detail"),
    path("customer_cases_videos/", CustomerCasesVideosListView.as_view(), name="customer_cases_videos-list"),
    path("customer_cases_videos/<int:pk>/", CustomerCasesVideosDetailView.as_view(),
         name="customer_cases_videos-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
