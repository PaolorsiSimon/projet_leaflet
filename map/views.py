from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.serializers import serialize
from map.models import PointInteret, Itineraire, TypePointInteret, PointDansItineraire

class MapPageView(TemplateView):
    template_name= 'map/map.html'

def pointsInteret_dataset(request):
    pointsInteret = serialize('geojson', PointInteret.objects.all())
    return HttpResponse(pointsInteret, content_type='json')


def type_point_dataset(request):
    type = serialize('json', TypePointInteret.objects.all())
    return HttpResponse(type, content_type='json')
# Create your views here.



from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from .models import Itineraire, PointInteret

def itineraires_dataset(request):
    # Récupérer tous les itinéraires
    itineraires = Itineraire.objects.all()

    # Générer les données GeoJSON
    features = []
    for itineraire in itineraires:
        # Générer la géométrie de l'itinéraire
        geometry = {
            "type": "LineString",
            "coordinates": list(itineraire.itineraire.coords),
        }

        # Générer les propriétés de l'itinéraire
        properties = {
            "scenario": itineraire.scenario,
            "commentaire": itineraire.commentaire,
            "depart": {
                "id": itineraire.depart_id,
                "nom": itineraire.depart.nom,
            },
            "arrivee": {
                "id": itineraire.arrivee_id,
                "nom": itineraire.arrivee.nom,
            },
        }

        # Générer la feature de l'itinéraire
        feature = {
            "type": "Feature",
            "id": itineraire.id,
            "properties": properties,
            "geometry": geometry,
        }

        # Ajouter la feature de l'itinéraire à la liste des features
        features.append(feature)

    # Générer la collection de features
    collection = {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {"name": "EPSG:4326"},
        },
        "features": features,
    }

    # Renvoie les données GeoJSON au format JSON
    return JsonResponse(
        collection,
        encoder=DjangoJSONEncoder,
        safe=False,
    )
