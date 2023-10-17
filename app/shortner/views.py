from django.shortcuts import render
import uuid
from shortner.models import Url
from extensions.utils import get_client_ip
from django.http import HttpResponse
import datetime


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
        while True:
            uid = str(uuid.uuid4())[:5]
            try:
                exist_uid = Url.objects.get(uuid=uid)
            except:
                break
        ip = get_client_ip(request)
        new_url = Url(link=url, uuid=uid, ip=ip, expire=datetime.date.today() + datetime.timedelta(days=2))
        new_url.save()
        return HttpResponse(uid)
