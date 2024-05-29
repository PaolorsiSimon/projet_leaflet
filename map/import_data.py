import django
django.setup()

from map.models import import_shapefile

shapefile_path = '/path/to/your/shapefile.shp'
import_shapefile(shapefile_path)