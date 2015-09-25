from rest_framework import serializers
from .models import Vinculacion, Proposito
 
class VinculacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculacion
        fields = ('id', 'vinculacion',)
 
class PropositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposito
        usuario = serializers.ReadOnlyField(source='usuario.username')
        fields = ('id', 'mes_ano', 'proposito','usuario')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    propositos = serializers.PrimaryKeyRelatedField(many=True, queryset=Proposito.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'propositos')
 