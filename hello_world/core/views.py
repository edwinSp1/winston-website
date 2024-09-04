from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ..settings import BASE_DIR
from ..models import Asset

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def download(file):
    path = f'{BASE_DIR}/hello_world/static/media/{file.name}'
    with open(path, 'wb+') as f:
        f.write(file.read())

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = request.POST
        files = request.FILES
        asset = files['asset']
        thumbnail = files['thumbnail']

        download(asset); download(thumbnail)

        Asset.objects.create(
            asset_type=form['type'], 
            asset_desc=form['description'],
            asset_loc=asset.name,
            thumbnail_loc=thumbnail.name
        )
        return HttpResponse('thanks bro. pon')

    return render(request, 'upload.html')

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