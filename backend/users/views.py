from .models import Users
from rest_framework import viewsets
from .serializer import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.object.all()
    serializer_class = UsersSerializer