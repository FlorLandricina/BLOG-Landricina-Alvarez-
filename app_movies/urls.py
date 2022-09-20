from django.urls import path
from app_movies import views
from app_movies.views import TituloListView


urlpatterns = [
    # Vistas con clases
    path('', views.TituloListView.as_view(), name = "peliculas"),
    path('crear-peliculas/', views.TituloCreateView.as_view(), name = "crear_peliculas"),
    path('editar-peliculas/<int:pk>/', views.TituloUpdateView.as_view(), name = "editar_peliculas"),
    path('eliminar-peliculas/<int:pk>/', views.TituloDeleteView.as_view(), name = "eliminar_peliculas"),
    
    # Busqueda titulo
    path('busqueda-titulo-form/', views.busqueda_titulo, name= "busqueda_titulo_form"),
    path('busqueda-titulo/', views.buscar, name= "busqueda_titulo"),

    # URLS Usuario y sesión
    path('login/', views.login_request, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),

    # URLS Perfil
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),

    # URL Mensajes
    path('messages/', views.mensajes, name="mensajes")
]