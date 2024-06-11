import os
from django.contrib.gis.utils import LayerMapping
from .models import CoursDeau

# Auto-generated `LayerMapping` dictionary for CoursDeau model
coursdeau_mapping = {
    'gid': 'gid',
    'cdentitehy': 'CdEntiteHy',
    'nomentiteh': 'NomEntiteH',
    'candidat': 'Candidat',
    'classe': 'Classe',
    'layer': 'layer',
    'path': 'path',
    'geom': 'MULTILINESTRING',
}
courseau_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), "C:/Users/sipao/Documents/MASTER/SEMESTRE_8/Django/projet_leaflet/fleuves.geojson"))

def run(verbose=True):
    lm = LayerMapping(CoursDeau, courseau_shp, coursdeau_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)