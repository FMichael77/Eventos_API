from rest_framework import serializers
from .models import Usuario, CategoriaEvento, Evento, Comentario
from django.contrib.auth.models import User


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(queryset=Usuario.objects.all(), slug_field='nome')
    evento = serializers.SlugRelatedField(queryset=Evento.objects.all(), slug_field='nome')
    
    class Meta:
        model = Comentario
        fields = ('pk', 'conteudo', 'usuario', 'evento')


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    categoria_evento = serializers.SlugRelatedField(queryset=CategoriaEvento.objects.all(), slug_field='nome')
    comentarios = ComentarioSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Evento
        fields = (
                'pk',
                'owner',
                'nome',
                'capacidade',
                'rua',
                'cidade',
                'cep',
                'categoria_evento',
                'comentarios'
            )
  
       
class CategoriaEventoSerializer(serializers.HyperlinkedModelSerializer):
    eventos = EventoSerializer(many=True, read_only=True)
    
    class Meta:
        model = CategoriaEvento
        fields = ('pk', 'nome', 'eventos')
   
        
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Usuario
        fields = (
                'pk',
                'nome',
                'email',
                'rua',
                'cidade',
                'cep'
            )

        
class UserEventoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Evento
        fields = (
                'pk',
                'nome'
            )
  
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    eventos = UserEventoSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = (
                'pk',
                'username',
                'eventos'
            )      
        