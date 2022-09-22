from ast import Return
from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from app_movies.models import Titulo
from app_movies.models import Genero, Rating, Mensajes
from app_movies.forms import TituloFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario, MensajesForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django import forms


def inicio(request):
    return render(request, "app_movies/inicio.html")
    
class TituloListView(LoginRequiredMixin, ListView):
    model = Titulo
    template_name = 'app_movies/movies_list.html'

class TituloCreateView(LoginRequiredMixin, CreateView):
    model = Titulo
    fields = ['nombre','ano_lanzamiento','rating','genero','cuerpo']
    success_url = reverse_lazy('peliculas')

class TituloUpdateView(LoginRequiredMixin, UpdateView):
    model = Titulo
    fields = ['nombre','ano_lanzamiento','rating','genero','cuerpo']
    success_url = reverse_lazy('peliculas')

class TituloDeleteView(LoginRequiredMixin, DeleteView):
    model = Titulo
    success_url = reverse_lazy('peliculas')


def busqueda_titulo(request):
    return render(request, "app_movies/form_busqueda_titulo.html")


def buscar(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        peliculas = Titulo.objects.filter(nombre__icontains=titulo)
        return render(request,"app_movies/movies_list.html",{"titulos":peliculas})
    else:
        return render(request,"app_movies/movies_list.html",{"titulo":[]})


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_movies/inicio.html", {"mensaje": "Se ha creado el usuario exitosamente"})
        else:
            mensaje = 'Se cometio un error en el registro'
    formulario = UserRegisterForm()
    context = {
        'form': formulario,
        'mensaje': mensaje
    }
    return render(request, "app_movies/registro.html", context=context)


def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "app_movies/inicio.html", {"mensaje":f"Bienvenido a la biblioteca cinematografica {usuario}"})
            else:
                return render(request,"app_movies/inicio.html", {"mensaje":"Ha ocurrido un error, datos incorrectos"})
        else:
            return render(request,"app_movies/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"app_movies/login.html", {'form':form} )

class CustomLogoutView(LogoutView):
    template_name = 'app_movies/logout.html'
    next_page = reverse_lazy('inicio')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'app_movies/registro.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid:
            avatar = form.save()
            avatar.user = request.user
            avatar.save()  
            return redirect(reverse('inicio'))

    form = AvatarFormulario()
    return render(request, "app_movies/form_avatar.html", {"form":form})



def about_me(request):
    return render(request, 'app_movies/about.html')


@login_required
def mensajes (request):

    mensajeForm = MensajesForm()
    mensaje = Mensajes.objects.all()
    if request.method == 'POST':
        contenido_mensaje = MensajesForm(request.POST)
        if contenido_mensaje.is_valid():
            data = contenido_mensaje.cleaned_data
            mensaje = Mensajes(mensaje=data["mensaje"], user=request.user)
            mensaje.save()
            return redirect('mensajes')
        else:
            return render(request, 'app_movies/mensajes.html', {"mensajeForm": contenido_mensaje,"mensajes": mensaje})
    else:
        return render(request, 'app_movies/mensajes.html', {"mensajeForm": mensajeForm,  "mensajes": mensaje})
