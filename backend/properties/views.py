from .models import Amenity,Property
from rest_framework import viewsets
from .serializer import AmenitySerializer,PropertySerializer

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.object.all()
    serializer_class = AmenitySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.object.all()
    serializer_class = PropertySerializer
    
