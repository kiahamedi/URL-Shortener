from django.shortcuts import render, redirect, get_object_or_404
import uuid
from shortner.models import Url, User
from extensions.utils import get_client_ip, sendSMS
from django.http import HttpResponse
import datetime
from django.utils import timezone
from django.http import JsonResponse
import random
from django_ratelimit.decorators import ratelimit

# Create your views here.
def home(request):
    context = {}
    return render(request, 'shortner/index.html', context)

def test404(request):
    context = {}
    return render(request, 'shortner/404.html', context)

def handler404(request, exception):
    context = {}
    response = render(request, "shortner/404.html", context=context)
    response.status_code = 404
    return response

def create(request):
    if request.method == "POST":
        url = request.POST['link']
        token = request.POST['userToken']
        bool_dict = {'true': True, 'false': False, 'True': True, 'False': False}
        is_expire = bool_dict.get(request.POST['is_expire'])
        days = request.POST['days']

        if User.objects.filter(access_token=token).exists():
            user = User.objects.get(access_token=token)
            while True:
                uid = str(uuid.uuid4())[:5]
                try:
                    exist_uid = Url.objects.get(uuid=uid)
                except:
                    break
            ip = get_client_ip(request)

            if is_expire:
                day = int(days.split(" ")[0])
                new_url = Url(link=url, uuid=uid, ip=ip, is_expire=is_expire, expire=datetime.datetime.today() + datetime.timedelta(days=day), submiter=user)
            else:
                new_url = Url(link=url, uuid=uid, ip=ip, is_expire=is_expire, submiter=user)
            new_url.save()
            return HttpResponse(uid)
        else:
            data = {
                    "status": "unsuccess",
                    "msg": "invalid token"
                }
            return JsonResponse(data)


def gourl(request, slug):
    url_info = get_object_or_404(Url, uuid=slug)
    if url_info.is_expire:
        if timezone.now() > url_info.expire:
            return render(request, 'shortner/404.html')
        else:
            return redirect(url_info.link)
    else:
        return redirect(url_info.link)


def login(request):
    context = {}
    return render(request, 'shortner/login.html', context)

# @ratelimit(key='ip', rate='10/m', block=True)
def login_or_register(request):
    if request.method == "POST":
        phone = request.POST['phone']

        otp = random.randint(1000, 9999)
        if User.objects.filter(phone=phone).exists():
            user = User.objects.get(phone=phone)
            user.ip = get_client_ip(request)
            user.otp = otp
            user.expire_otp = datetime.datetime.today() + datetime.timedelta(hours=1)
            user.save()

        else:
            user = User.objects.create(
                phone=phone,
                ip = get_client_ip(request),
                otp = str(otp),
                expire_otp = datetime.datetime.today() + datetime.timedelta(hours=1)
            )
        
        # Todo: Send sms OTP
        sendSMS(phone, otp)
        data = {
            "phone": phone,
            "status": "success"
        }
        return JsonResponse(data)


def verify_otp(request):
    if request.method == "POST":
        phone = request.POST['phone']
        otp = request.POST['otp']

        if User.objects.filter(phone=phone).exists():
            user = User.objects.get(phone=phone)

            # if timezone.now() > user.expire_otp:
            if str(user.otp) == str(otp):
                token = str(uuid.uuid4())

                user.status = 'a'
                user.access_token = token
                user.save()
                
                data = {
                    "token": token,
                    "status": "success"
                }
                return JsonResponse(data)
            else:
                data = {
                    "status": "unsuccess",
                    "msg": "invalid code"
                }
                return JsonResponse(data)
            # else:
            #     data = {
            #         "status": "unsuccess",
            #         "msg": "expire your code"
            #     }
            return JsonResponse(data)
        else:
            data = {
                "status": "unsuccess",
                "msg": "not found"
            }
            return JsonResponse(data)