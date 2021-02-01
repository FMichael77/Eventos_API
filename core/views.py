from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django.contrib.auth.models import User
from .models import Usuario, CategoriaEvento, Evento, Comentario
from .serializers import UsuarioSerializer, CategoriaEventoSerializer, EventoSerializer, ComentarioSerializer, UserSerializer
from core.permissions import IsOwnerOrReadOnly


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'Realizadores'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly),


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'Realizadores-Detalhes'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CategoriaEventoList(generics.ListCreateAPIView):
    queryset = CategoriaEvento.objects.all()
    serializer_class = CategoriaEventoSerializer
    name = 'Categoria-Eventos'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly),
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['nome']


class CategoriaEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaEvento.objects.all()
    serializer_class = CategoriaEventoSerializer
    name = 'Categoria-Eventos-Detalhes'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser,)


class EventoList(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    name = 'Eventos'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    throttle_scope = 'evento'
    throttle_classes = (ScopedRateThrottle),
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['nome', 'categoria_evento']
    ordering = ['nome']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    name = 'Eventos-Detalhes'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    throttle_scope = 'evento'
    throttle_classes = (ScopedRateThrottle),


class ComentarioList(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    name = 'Comentarios'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly),

    def get_queryset(self):
        queryset = Comentario.objects.filter(evento=self.kwargs.get('evento'))
        return queryset


class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    name = 'Domentarios-Detalhes'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Comentario.objects.filter(evento=self.kwargs.get('evento'))
        return queryset


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'User-List'
    permission_classes = (permissions.IsAuthenticated),


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'User-Detail'
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,)


class ApiRoot(generics.GenericAPIView):
    name = 'API-Root'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly),

    def get(self, request, *args, **kwargs):
        return Response({
            'Realizadores': reverse(UsuarioList.name, request=request),
            'Eventos': reverse(EventoList.name, request=request),
            'Categorias': reverse(CategoriaEventoList.name, request=request),
            'Users': reverse(UserList.name, request=request),
        })
