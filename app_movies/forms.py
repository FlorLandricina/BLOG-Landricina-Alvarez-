from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_movies.models import Avatar

class TituloFormulario (forms.Form):
    nombre = forms.CharField(max_length=150)
    ano_lanzamiento = forms.DateField()
    rating = forms.ModelMultipleChoiceField(queryset=models.Rating.objects.all(), widget=forms.CheckboxSelectMultiple)
    genero = forms.ModelMultipleChoiceField(queryset=models.Genero.objects.all(), widget=forms.CheckboxSelectMultiple)
    cuerpo = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 12}))
    portada= forms.ImageField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class MensajesForm(forms.Form):
    mensaje = forms.CharField(max_length=400)