from django.contrib.auth import views
from django.urls import path
from shortner.views import (
    home,
    create,
    gourl,
    test404,
)
from django.views.decorators.csrf import csrf_exempt


app_name = "dashboard"

urlpatterns = [
    path('', home, name="home"),
    path('create/', csrf_exempt(create), name="create"),
    path('<slug:slug>', gourl, name="gourl"),
    path('test404/', test404, name="test404"),
]