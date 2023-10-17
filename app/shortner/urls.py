from django.contrib.auth import views
from django.urls import path
from shortner.views import (
    home,
    test404
)


app_name = "dashboard"

urlpatterns = [
    path('', home, name="home"),
    path('test404/', test404, name="test404"),
]