from django.contrib.auth import views
from django.urls import path
from shortner.views import (
    home
)


app_name = "dashboard"

urlpatterns = [
    path('', home, name="home"),
]