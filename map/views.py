from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from django.core.serializers import serialize
from map.models import PointInteret, Itineraire, TypePointInteret, PointDansItineraire
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import LoireModel, Itineraire, PointInteret


# def creer_itineraire(request):
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         loire_gid = request.POST['loire_gid']
#         depart_pk = request.POST['depart_pk']
#         arrivee_pk = request.POST['arrivee_pk']
#         scenario = request.POST['scenario']
#         commentaire = request.POST.get('commentaire')

#         # Récupérer les objets LoireModel, PointInteret de départ et d'arrivée
#         loire_obj = get_object_or_404(LoireModel, gid=loire_gid)
#         depart_obj = get_object_or_404(PointInteret, pk=depart_pk)
#         arrivee_obj = get_object_or_404(PointInteret, pk=arrivee_pk)

#         # Découper la géométrie dans LoireModel en fonction des points de départ et d'arrivée
#         itineraire_django = decouper_itineraire(loire_obj, depart_obj, arrivee_obj)

#         # Créer un nouvel objet Itineraire
#         nouvel_itineraire = Itineraire.objects.create(
#             itineraire=itineraire_django,
#             scenario=scenario,
#             commentaire=commentaire,
#             depart=depart_obj,
#             arrivee=arrivee_obj,
#             loire_gid=loire_obj.gid,
#         )

#         # Ajouter un message de succès
#         messages.success(request, 'L\'itinéraire a été créé avec succès.')

#         # Rediriger vers la page de détail de l'itinéraire
#         return redirect('itineraire_detail', pk=nouvel_itineraire.pk)

#     else:
#         # Récupérer la liste des objets LoireModel et PointInteret pour afficher dans le formulaire
#         loire_models = LoireModel.objects.all()
#         point_interets = PointInteret.objects.all()

#         # Rendre le formulaire de création d'itinéraire
#         return render(request, 'creer_itineraire.html', {
#             'loire_models': loire_models,
#             'point_interets': point_interets,
#         })
















class MapPageView(TemplateView):
    template_name= 'map/map.html'

def pointsInteret_dataset(request):
    pointsInteret = serialize('geojson', PointInteret.objects.all())
    return HttpResponse(pointsInteret, content_type='json')


def type_point_dataset(request):
    type = serialize('json', TypePointInteret.objects.all())
    return HttpResponse(type, content_type='json')
# Create your views here.



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
