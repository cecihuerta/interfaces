from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Enfermedad)
admin.site.register(Paciente)
admin.site.register(Alimento)
admin.site.register(Preparacion)
admin.site.register(Dieta)