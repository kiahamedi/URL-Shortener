from django.shortcuts import render


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