from .models import Vinculacion, Proposito
from .serializers import PropositoSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from mainApp.serializers import UserSerializer
 



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    