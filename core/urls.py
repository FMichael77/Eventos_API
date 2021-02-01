from django.contrib import admin
from django.urls import include, path
from core import views
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Eventos API",
      default_version='v1',
      description="API voltada para organização e participação de eventos.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@eventosAPI.local"),
      license=openapi.License(name="EventosAPI License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    path('usuarios/', views.UsuarioList.as_view(),
        name=views.UsuarioList.name),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(),
        name=views.UsuarioDetail.name),
    path('categorias/', views.CategoriaEventoList.as_view(),
        name=views.CategoriaEventoList.name),
    path('categorias/<int:pk>/', views.CategoriaEventoDetail.as_view(),
        name=views.CategoriaEventoDetail.name),
    path('eventos/', views.EventoList.as_view(),
        name=views.EventoList.name),
    path('eventos/<int:pk>', views.EventoDetail.as_view(),
        name=views.EventoDetail.name),
    path('eventos/<int:evento>/comentarios/', views.ComentarioList.as_view(),
        name=views.ComentarioList.name),
    path('eventos/<int:evento>/comentarios/<int:pk>', views.ComentarioDetail.as_view(),
        name=views.ComentarioDetail.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('login/', obtain_jwt_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
