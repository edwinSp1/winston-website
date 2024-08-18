from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..settings import BASE_DIR

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        path = f'{BASE_DIR}/hello_world/media/{file.name}'
        with open(path, 'wb+') as f:
            f.write(file.read())
    return HttpResponse('thanks bro. pon')

def assets2D(req):
    context = {
        "title": "Free Asset Bazaar",
        'assets_fileLOC': ["a,"],
        'type': '2D'
    }
    return render(req, 'assets.html', context)

def assets3D(req):
    context = {
        "title": "Free Asset Bazaar",
        'assets_fileLOC': ["a,"],
        'type': '3D'
    }
    return render(req, 'assets.html', context)
def donate(request):
    context = {
        "title": "Free Asset Bazaar",
    }
    return render(request, "donate.html", context)
def about(request):
    context = {
        "title": "Free Asset Bazaar",
    }
    return render(request, "about.html", context)