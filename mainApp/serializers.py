from rest_framework import serializers
from .models import Vinculacion, Proposito, Marcacion, UserPerfil , Oracion
from django.contrib.auth.models import User
 

class MarcacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcacion
        #usuario = serializers.ReadOnlyField(source='usuario.username')

        fields = ('id', 'dia', 'cumplimiento', 'proposito')


class UserPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPerfil
        #usuario = serializers.ReadOnlyField(source='usuario.username')

        fields = ('nacimiento', 'pais', 'ideal_personal','reafirmar', 'liberar', 'adquirir', , 'idioma')


class PropositoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    marcaciones = MarcacionSerializer(many=True,required=False)

    class Meta:
        model = Proposito


        fields = ('id', 'usuario', 'vinculacion', 'proposito', 'mes_ano',  'marcaciones')







 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],

        )
        user.set_password(validated_data['password'])
        user.save()
        userprofile = UserPerfil(user = user);
        return user

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],

        )
        user.set_password(validated_data['password'])
        user.save()
        userprofile = UserPerfil(user = user);
        return user



class OracionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oracion
        fields = ('nombre', 'contenido')

class OracionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oracion
        fields = ('id','nombre',)

