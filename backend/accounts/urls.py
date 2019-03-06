from django.conf.urls import url
from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    url(r"login/$", views.login),
    url(r"^token/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]
