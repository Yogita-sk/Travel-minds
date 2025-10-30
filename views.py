from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# View for the Home page
def home(request):
    places = PlaceImage.objects.all()
    context = {
        'places': places
    }
    return render(request, 'index.html', context)

# View for the About page
def about(request):
    return render(request, 'about.html')

# View for the Makeroot page
def makeroot(request):
    return render(request, 'makeYourRoute.html')

# View for the Localdata page
def localdata(request):
    return render(request, 'local_data_map.html')
