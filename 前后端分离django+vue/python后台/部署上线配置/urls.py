"""hg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'products': reverse("products:products-list", request=request, format=format),
            'home_encyclopedias': reverse("home_encyclopedias:home_encyclopedias-list", request=request, format=format),
            'consulting_news': reverse("consulting_news:consulting_news-list", request=request, format=format),
            "customer_cases": reverse("customer_cases:customer_cases-list", request=request, format=format),
        }
    )


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("media/<path:path>", serve, {'document_root': settings.MEDIA_ROOT}),
    path("static/<path:path>", serve, {"document_root": settings.STATIC_ROOT}),
    path('', include(("apps.customer_cases.urls", "customer_cases"), namespace="customer_cases")),
    path('', include(("apps.consulting_news.urls", "consulting_news"), namespace="consulting_news")),
    path('', include(("apps.products.urls", 'products'), namespace='products')),
    path('', include(("apps.home_encyclopedias.urls", "home_encyclopedias"), namespace="home_encyclopedias")),
]
