import os
from django.contrib.gis.utils import LayerMapping
from .models import CoursDeau

# Auto-generated `LayerMapping` dictionary for CoursDeau model
coursdeau_mapping = {
    'geo_point_2d': 'geo_point_2d',
    'id': 'id',
    'prec_plani': 'prec_plani',
    'prec_alti': 'prec_alti',
    'artif': 'artif',
    'fictif': 'fictif',
    'franchisst': 'franchisst',
    'nom': 'nom',
    'pos_sol': 'pos_sol',
    'regime': 'regime',
    'z_ini': 'z_ini',
    'z_fin': 'z_fin',
    'commune': 'commune',
    'code_insee': 'code_insee',
    'epci_name': 'epci_name',
    'dep_name': 'dep_name',
    'reg_name': 'reg_name',
    'geom': 'MULTILINESTRING25D',
}

coursDeau_geojson = os.path .abspath(os.path.join(os.path.dirname(__file__), "C:/Users/sipao/Documents/MASTER/SEMESTRE_8/Django/projet_leaflet/hydrographie-cours-deau.geojson"))

def import_data(verbose=True):
    lm = LayerMapping(CoursDeau, coursDeau_geojson, coursdeau_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)