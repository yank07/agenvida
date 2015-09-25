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


from mainApp.models import Proposito
from mainApp.permissions import IsOwnerOrReadOnly

from mainApp.serializers import PropositoSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

##############VERSION 1 DEL API##############################


# @csrf_exempt
# def proposito_list(request):
#     """
#     List all code propositos, or create a new proposito.
#     """
#     if request.method == 'GET':
#         propositos = Proposito.objects.all()
#         serializer = PropositoSerializer(propositos, many=True)
#         return JSONResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PropositoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)


# @csrf_exempt
# def proposito_detail(request, pk):
#     """
#     Retrieve, update or delete a code proposito.
#     """
#     try:
#         proposito = Proposito.objects.get(pk=pk)
#     except Proposito.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = PropositoSerializer(proposito)
#         return JSONResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PropositoSerializer(proposito, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         proposito.delete()
#         return HttpResponse(status=204)


##############VERSION 2 DEL API##############################3

# @api_view(['GET', 'POST'])
# def proposito_list(request, format=None):
#     """
#     List all propositos, or create a new proposito.
#     """
#     if request.method == 'GET':
#         propositos = Proposito.objects.all()
#         serializer = PropositoSerializer(propositos, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PropositoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








# @api_view(['GET', 'PUT', 'DELETE'])
# def proposito_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a proposito instance.
#     """
#     try:
#         proposito = Proposito.objects.get(pk=pk)
#     except Proposito.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PropositoSerializer(proposito)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PropositoSerializer(proposito, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         proposito.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



##############VERSION 3 DEL API##############################


class PropositoList(APIView):
    """
    List all propositos, or create a new proposito.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    def get(self, request, format=None):
        propositos = Proposito.objects.all()
        serializer = PropositoSerializer(propositos, many=True)
        self.check_object_permissions(request, propositos)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropositoSerializer(data=request.data)
        self.check_permissions(self, request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)



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
