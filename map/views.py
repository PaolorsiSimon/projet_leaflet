from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from django.core.serializers import serialize
from map.models import Glossaire, PointInteret, Itineraire, TypePointInteret, PointDansItineraire

class MapPageView(TemplateView):
    template_name= 'map/map.html'

def pointsInteret_dataset(request):
    pointsInteret = serialize('geojson', PointInteret.objects.all())
    return HttpResponse(pointsInteret, content_type='json')


def type_point_dataset(request):
    type = serialize('json', TypePointInteret.objects.all())
    return HttpResponse(type, content_type='json')
# Create your views here.


#AJOUTER LES VIEWS POUR LE FRONT
def home(request):
    return render(request, 'map/home.html')
def glossaire(request):
    
    ##Début ajout formulaire V2
    from .forms import FormulaireRecherche
    from .models import Glossaire
    
    resultat = None
    non_trouve = False

    if request.method == 'POST':
        form = FormulaireRecherche(request.POST)
        if form.is_valid():
            mot = form.cleaned_data['mot']
            try:
                resultat = Glossaire.objects.get(mot__iexact=mot)
            except Glossaire.DoesNotExist:
                non_trouve = True
    else:
        form = FormulaireRecherche()

    return render(request, 'map/glossaire.html', {'form': form, 'resultat': resultat, 'non_trouve': non_trouve})

    ##Fin ajout formulaire V2"""
    
    #glossaire = Glossaire.objects.all()
    #context = {'glossaire': glossaire,}
    #return render (request, 'map/glossaire.html', context)



def liens(request):
    return render(request, 'map/liens.html')

def contacts(request):
    return render(request, 'map/contacts.html')

