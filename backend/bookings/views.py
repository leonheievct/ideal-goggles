from .models import BlockedDate,Bookings
from rest_framework import viewsets
from .serializer import BlockedDateSerializer,BookingsSerializer

class BlockedDateViewSet(viewsets.ModelViewSet):
    queryset = BlockedDate.object.all()
    serializer_class = BlockedDateSerializer

class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Bookings.object.all()
    serializer_class = BookingsSerializer
    




