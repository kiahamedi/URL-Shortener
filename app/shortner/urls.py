from django.contrib.auth import views
from django.urls import path
from shortner.views import (
    home,
    create,
    gourl,
    test404,
    login,
    login_or_register,
    verify_otp
)
from django.views.decorators.csrf import csrf_exempt


app_name = "dashboard"

urlpatterns = [
    path('', home, name="home"),
    path('create/', csrf_exempt(create), name="create"),
    path('<slug:slug>', gourl, name="gourl"),
    path('test404/', test404, name="test404"),
    path('login/', login, name="login"),
    path('login_or_register/', csrf_exempt(login_or_register), name="login_or_register"),
    path('verify_otp/', csrf_exempt(verify_otp), name="verify_otp"),
]