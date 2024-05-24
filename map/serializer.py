from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Itineraire

class ItineraireSerializer(GeoFeatureModelSerializer):
    depart = serializers.SerializerMethodField()
    arrivee = serializers.SerializerMethodField()

    class Meta:
        model = Itineraire
        geo_field = "itineraire"
        fields = ('id', 'itineraire', 'scenario', 'depart', 'arrivee')

    def get_depart(self, obj):
        return str(obj.depart) if obj.depart else None

    def get_arrivee(self, obj):
        return str(obj.arrivee) if obj.arrivee else None
