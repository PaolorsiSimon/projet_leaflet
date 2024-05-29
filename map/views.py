from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.serializers import serialize
from map.models import PointInteret, Itineraire, TypePointInteret, PointDansItineraire

#AJOUTER LES VIEWS POUR LE FRONT
def home(request):
    return render(request, 'home.html')





class MapPageView(TemplateView):
    template_name= 'map/map.html'

def pointsInteret_dataset(request):
    pointsInteret = serialize('geojson', PointInteret.objects.all())
    return HttpResponse(pointsInteret, content_type='json')

def itineraires_dataset(request):
    itineraires = serialize('geojson', Itineraire.objects.all())
    return HttpResponse(itineraires, content_type='json')

def type_point_dataset(request):
    type = serialize('json', TypePointInteret.objects.all())
    return HttpResponse(type, content_type='json')
# Create your views here.

