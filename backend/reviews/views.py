from .models import Reviews
from rest_framework import viewsets
from .serializer import ReviewsSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.object.all()
    serializer_class = ReviewsSerializer
    
