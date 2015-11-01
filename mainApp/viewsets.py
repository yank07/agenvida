from .models import Vinculacion, Proposito, Oracion
from .serializers import PropositoSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from mainApp.serializers import UserSerializer, OracionSerializer
 



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


