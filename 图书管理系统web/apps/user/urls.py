from django.urls import path
from .views import UserCenterView, UserLogoutView


urlpatterns = [
    path('center/', UserCenterView.as_view(), name="center"),
    path('center/<path:type>', UserCenterView.as_view(), name="center_type"),

    # path('rental/', UserRentalView.as_view(), name="rental"),
    # path('rental/<int:page>', UserRentalView.as_view(), name="rental_page"),

    path('logout/', UserLogoutView.as_view(), name="logout"),
]
