from django.shortcuts import render, redirect, get_object_or_404
import uuid
from shortner.models import Url
from extensions.utils import get_client_ip
from django.http import HttpResponse
import datetime
from django.utils import timezone


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
        bool_dict = {'true': True, 'false': False, 'True': True, 'False': False}
        is_expire = bool_dict.get(request.POST['is_expire'])
        days = request.POST['days']

        while True:
            uid = str(uuid.uuid4())[:5]
            try:
                exist_uid = Url.objects.get(uuid=uid)
            except:
                break
        ip = get_client_ip(request)

        if is_expire:
            day = int(days.split(" ")[0])
            new_url = Url(link=url, uuid=uid, ip=ip, is_expire=is_expire, expire=datetime.datetime.today() + datetime.timedelta(days=day))
        else:
            new_url = Url(link=url, uuid=uid, ip=ip, is_expire=is_expire)
        new_url.save()
        return HttpResponse(uid)


def gourl(request, slug):
    url_info = get_object_or_404(Url, uuid=slug)
    if url_info.is_expire:
        if timezone.now() > url_info.expire:
            return render(request, 'shortner/404.html')
        else:
            return redirect(url_info.link)
    else:
        return redirect(url_info.link)