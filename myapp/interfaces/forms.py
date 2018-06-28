from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Enfermedad

class SignUpForm(forms.Form):
	username = forms.CharField(label='Usuario')
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
	email = forms.EmailField()
	nombre = forms.CharField()
	apellido = forms.CharField()
	edad = forms.IntegerField()
	enfermedad = forms.ModelMultipleChoiceField(help_text='Mantenga la tecla control apretada para agregar o quitar enfermedades.', label='Enfermedad(es)',queryset=Enfermedad.objects.all(), required=False)
	estatura = forms.FloatField(help_text='En metros')
	max_permitido = forms.IntegerField(help_text='Maxima cantidad de calorias que puede ingerir por día.',required=False)

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)


"""
class SignUpForm(UserCreationForm):
	nombre = forms.CharField()
	apellido = forms.CharField()
	edad = forms.IntegerField(help_text='Required')
	enfermedad = forms.ModelChoiceField(label='Enfermedad(es)', queryset=Enfermedad.objects.all())
	estatura = forms.FloatField()
	max_permitido = forms.IntegerField(help_text='Maxima cantidad de calorias que puede ingerir por día.',required=False)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'edad', 'enfermedad', 'estatura', 'max_permitido')
"""