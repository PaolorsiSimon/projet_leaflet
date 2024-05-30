from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.serializers import serialize
from map.models import Glossaire, PointInteret, Itineraire, TypePointInteret, PointDansItineraire

#AJOUTER LES VIEWS POUR LE FRONT
def home(request):
    return render(request, 'map/home.html')

def doc(request):
    return render(request, 'map/doc.html')


#VERIFIER LA VUE CI DESSOUS
def glossaire(request):
    from map.forms import FormulaireRecherche

    resultat = Glossaire.objects.all()

    if request.method == 'POST' :
        Glossaire = FormulaireRecherche (request.POST)
        if request.POST.get('Metier'):
                param_type = request.POST.get('Metier')
                resultats = resultats.filter (fk_type=param_type)
        if request.POST.get('Personnage'):
                param_type = request.POST.get('Personnage')
                resultats = resultats.filter (fk_type=param_type)
        if request.POST.get('Materiaux'):
                param_type = request.POST.get('Materiaux')
                resultats = resultats.filter (fk_type=param_type)
    
    else : Glossaire = FormulaireRecherche() 

    context = {
        'resultats' : resultats,
        'formulaire' : Glossaire
    }

    return render(request, 'map/glossaire.html',context)




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

