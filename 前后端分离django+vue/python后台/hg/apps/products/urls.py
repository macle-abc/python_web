from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductsListView, ProductsDetailView, ProductsImagesDetailView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name="products-list"),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name="products-detail"),
    path('products_images/<int:pk>/', ProductsImagesDetailView.as_view(), name="products_images-detail"),
    # path('products/categories/', ProductsCategoriesView.as_view(), name="products_categories"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
