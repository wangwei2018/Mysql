from django.urls import re_path
from . import views

urlpatterns = [
    re_path("auth/login/", views.auth_login, name="login"),
    re_path("auth/register/", views.auth_register, name="register"),
    re_path("auth/logout/", views.auth_logout, name="logout"),
]
