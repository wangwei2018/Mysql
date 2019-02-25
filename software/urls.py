from django.urls import re_path
from . import views

urlpatterns = [
    re_path("software/improve/", views.improve, name="improve"),
    re_path("software/sendcode/", views.sendcode, name="sendcode"),
    re_path("software/upgrade/", views.upgratesoft, name="upgrade"),
    re_path("software/save/", views.save, name="save"),
    re_path("software/myorder/", views.myorder, name="myorder"),
]
