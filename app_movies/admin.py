from django.contrib import admin
from app_movies.models import Titulo, Genero, Rating, Avatar, Mensajes

admin.site.register(Titulo)
admin.site.register(Genero)
admin.site.register(Rating)
admin.site.register(Avatar)
admin.site.register(Mensajes)
