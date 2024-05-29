import os
from django.contrib.gis.utils import LayerMapping
from .models import LoireModel

# Auto-generated `LayerMapping` dictionary for LoireModel model
LoireModel_mapping = {
    'gid': 'gid',
    'cdentitehy': 'CdEntiteHy',
    'nomentiteh': 'NomEntiteH',
    'candidat': 'Candidat',
    'classe': 'Classe',
    'geom': 'MULTILINESTRING',
}

LoireModel_geojson = os.path .abspath(os.path.join(os.path.dirname(__file__), "C:/Users/sipao/Documents/MASTER/SEMESTRE_8/Django/projet_leaflet/test.geojson"))

def import_data(verbose=True):
    lm = LayerMapping(LoireModel, LoireModel_geojson, LoireModel_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)