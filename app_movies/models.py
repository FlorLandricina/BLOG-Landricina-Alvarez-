from pickle import TRUE
from django.db import models
from http.client import HTTPResponse
from datetime import date
from django.contrib.auth.models import User

class Titulo(models.Model):
    nombre = models.CharField(max_length=150)
    ano_lanzamiento = models.DateField()
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE, null=True)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE, null=True)
    cuerpo = models.TextField(max_length=1000, null=True)
    portada= models.ImageField(upload_to = 'post_images', null = True, blank = True)
    

    def __str__(self):
        return f"{self.nombre}"

        
class Rating(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.rating}"

class Genero(models.Model):
    genero = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.genero}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

class Mensajes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=400)
    def __str__(self):
        return f"id: {self.id}, user: {self.user}, mensaje: {self.mensaje}"
