from .models import Vinculacion, Proposito
from .serializers import PropositoSerializer, VinculacionSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from mainApp.serializers import UserSerializer
 
class VinculacionViewSet(viewsets.ModelViewSet):
 
    serializer_class = VinculacionSerializer
    queryset = Vinculacion.objects.all()
 
class PropositoViewSet(viewsets.ModelViewSet):
 
    serializer_class = PropositoSerializer
    queryset = Proposito.objects.all()





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    