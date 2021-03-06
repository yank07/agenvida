from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404 
from rest_framework.views import APIView
from rest_framework import permissions


from mainApp.models import Proposito, Vinculacion, Marcacion, UserPerfil, Oracion
from mainApp.permissions import IsOwnerOrReadOnly

from mainApp.serializers import PropositoSerializer, MarcacionSerializer, UserSerializer, UserPerfilSerializer, UserCreateSerializer, OracionSerializer, OracionListSerializer

from django.contrib.auth.models import User





##############VERSION 3 DEL API##############################

##########################################
############ PROPOSITO API ###############
#############################################

class PropositoList(APIView):
    """
    List all propositos, or create a new proposito.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    def get(self, request, format=None):
        propositos = Proposito.objects.filter(usuario=request.user)
        serializer = PropositoSerializer(propositos, many=True)
        self.check_object_permissions(request, propositos)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropositoSerializer(data=request.data)
        self.check_permissions(request)
        if serializer.is_valid():
            serializer.save(usuario=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
    	serializer.save(usuario=self.request.user)



class PropositoDetail(APIView):
    """
    Retrieve, update or delete a proposito instance.
    """
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    def get_object(self, pk):
		try:
			obj = Proposito.objects.get(pk=pk)
		except Propositos.DoesNotExist:
			raise Http404
		self.check_object_permissions(self.request, obj)
		return obj


    def get(self, request, pk, format=None):
        proposito = self.get_object(pk)
        serializer = PropositoSerializer(proposito)        
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        proposito = self.get_object(pk)
        self.check_object_permissions(request, proposito)
        serializer = PropositoSerializer(proposito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proposito = self.get_object(pk)
        self.check_object_permissions(request, proposito)
        proposito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



##########################################
############ MARCACION API ###############
#############################################
class MarcacionDetail(APIView):
    """
    Retrieve, update or delete a proposito instance.
    """
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    def get_object(self, pk):
        try:
            obj = Marcacion.objects.get(pk=pk)
        except Marcacion.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj


    def get(self, request, pk, format=None):
        marcacion = self.get_object(pk)
        serializer = MarcacionSerializer(marcacion)        
        return Response(serializer.data)
        

    def put(self, request, pk, format=None):
        marcacion = self.get_object(pk)
        self.check_object_permissions(request, marcacion)
        serializer = MarcacionSerializer(marcacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        marcacion = self.get_object(pk)
        self.check_object_permissions(request, marcacion)
        marcacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MarcacionList(APIView):
    """
    List all marcaciones, or create a new marcacion.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    def get(self, request, format=None):
        marcaciones = Marcacion.objects.filter(usuario=request.user)
        serializer = MarcacionSerializer(marcaciones, many=True)
        self.check_object_permissions(request, marcaciones)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MarcacionSerializer(data=request.data)
        self.check_permissions(request)
        if serializer.is_valid():
            serializer.save(usuario=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


###################################################
##########USER######################################
####################################################


class UserList(APIView):
    """
    List all usuarios, or create a new marcacion.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, user):
        try:
            obj = User.objects.get( id = user.id)
        except User.DoesNotExist:       
             obj = User.objects.create( user)
            
       
        return obj

    def get(self, request, format=None):
        users = self.get_object(request.user)
        serializer = UserSerializer(users)
        self.check_object_permissions(request, users)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
       ## self.check_permissions(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        user = self.get_object( request.user)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

class UserCreate(APIView):
    """
    List all usuarios, or create a new marcacion.
    """
  #  permission_classes = (permissions.IsAuthenticated,)
   

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
       ## self.check_permissions(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def perform_create(self, serializer):
        serializer.save()






class UserPerfilDetail(APIView):
    """
    Retrieve, update or delete a proposito instance.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, user):
        try:
            obj = UserPerfil.objects.get(user = user)
        except UserPerfil.DoesNotExist:       
             obj = UserPerfil.objects.create(user = user)
             print "Cree el usuario"
       
        return obj


    def get(self, request, format=None):
        userProfile = self.get_object(user = request.user)
        self.check_object_permissions(request, userProfile)
        serializer = UserPerfilSerializer(userProfile)        
        return Response(serializer.data)
        

    def put(self, request, format=None):
        userProfile = self.get_object( request.user)
        self.check_object_permissions(request, userProfile)
        serializer = UserPerfilSerializer(userProfile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  

##########################################
############ ORACION API ###############
#############################################

class OracionList(APIView):
    """
    List all oraciones, or create a new oracion.
    """
    #permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    def get(self, request, format=None):
        oraciones = Oracion.objects.all().order_by('nombre')
        serializer = OracionListSerializer(oraciones, many=True)
        self.check_object_permissions(request, oraciones)
        return Response(serializer.data)




class OracionDetail(APIView):
    """
    Retrieve, update or delete a oracion instance.
    """
    #permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    def get_object(self, pk):
        try:
            obj = Oracion.objects.get(pk=pk)
        except Oracions.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj


    def get(self, request, pk, format=None):
        oracion = self.get_object(pk)
        serializer = OracionSerializer(oracion)        
        return Response(serializer.data)
        

   

