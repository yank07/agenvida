from rest_framework import serializers
from .models import Vinculacion, Proposito, Marcacion
from django.contrib.auth.models import User
 

class MarcacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcacion
        #usuario = serializers.ReadOnlyField(source='usuario.username')

        fields = ('id', 'dia', 'cumplimiento', 'proposito')



class PropositoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    marcaciones = MarcacionSerializer(many=True,required=False)

    class Meta:
        model = Proposito


        fields = ('id', 'usuario', 'vinculacion', 'proposito', 'mes_ano',  'marcaciones')







class UserSerializer(serializers.ModelSerializer):
    #propositos = PropositoSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'propositos')
 