from django.db import models
from django.contrib.auth.models import User

class Enfermedad(models.Model):
	nombre = models.CharField(max_length=63)

	def __str__(self):
		return self.nombre

class Paciente(models.Model):
	cuenta = models.OneToOneField(User, on_delete=models.CASCADE)
	edad = models.IntegerField(default = 0)
	enfermedad = models.ManyToManyField(Enfermedad)
	estatura = models.FloatField(default=0.0)
	max_permitido = models.IntegerField(default=0)

	def __str__(self):
		return self.nombre + ' ' + self.apellido

class Informacion(models.Model):
	calorias = models.FloatField(null=True, blank=True)
	sodio = models.FloatField(null=True, blank=True)
	potacio = models.FloatField(null=True, blank=True)
	
class Alimento(models.Model):
	nombre = models.CharField(max_length=31)
	informacion = models.OneToOneField(Informacion, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


class Preparacion(models.Model):
	nombre = models.CharField(max_length=31)
	pertenece_a = models.ForeignKey(Paciente,on_delete=models.CASCADE)
	compuesto_por = models.ManyToManyField(Alimento)

	def __str__(self):
		return self.nombre

class Dieta(models.Model):
	user = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
	nombre = models.CharField(max_length=31)

	def __str__(self):
		return self.nombre

class preparacion_hora(models.Model):

	DIAS = (
	    (1, 'Lunes'),
	    (2, 'Martes'),
	    (3, 'Miércoles'),
	    (4, 'Jueves'),
	    (5, 'Viernes'),
	    (6, 'Sábado0'),
	    (7, 'Domingo'),
	)

	user = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
	dieta = models.ManyToManyField(Dieta)
	dia = models.CharField(
		max_length=2,
		choices=DIAS,
		default=1)
	time = models.TimeField()
	preparacion = models.ManyToManyField(Preparacion)

	def __str__(self):
		return self.dieta.nombre + ' ' + self.preparacion.nombre + ' ' + str(self.time)

