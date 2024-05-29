from geojson import Feature, FeatureCollection, LineString, MultiLineString, Point
from shapely.wkt import loads

def decouper_itineraire(loire_obj, depart, arrivee):
    # Convertir les points de départ et d'arrivée en objets Shapely Point
    depart_shapely = Point(depart.x, depart.y)
    arrivee_shapely = Point(arrivee.x, arrivee.y)

    # Convertir la géométrie de l'objet Loire en objet Shapely MultiLineString
    loire_shapely = loads(loire_obj.geom.ewkt)

    # Trouver le segment de ligne le plus proche du point de départ
    segment_depart = None
    distance_min = float('inf')
    for segment in loire_shapely:
        distance = segment.distance(depart_shapely)
        if distance < distance_min:
            distance_min = distance
            segment_depart = segment

    # Trouver le segment de ligne le plus proche du point d'arrivée
    segment_arrivee = None
    distance_min = float('inf')
    for segment in loire_shapely:
        distance = segment.distance(arrivee_shapely)
        if distance < distance_min:
            distance_min = distance
            segment_arrivee = segment

    # Découper la géométrie en fonction des segments de ligne trouvés
    itineraire_shapely = MultiLineString([segment for segment in loire_shapely if segment.intersects(segment_depart) and segment.intersects(segment_arrivee)])

    # Convertir l'objet Shapely MultiLineString en objet Django LineStringField
    itineraire_django = LineString(list(zip(*itineraire_shapely.xy)), srid=4326)


    return itineraire_django



