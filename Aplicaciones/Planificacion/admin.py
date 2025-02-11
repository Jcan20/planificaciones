from django.contrib import admin
from .models import Constructora,Cliente,Vivienda,Actividad
# Register your models here.
admin.site.register(Constructora)
admin.site.register(Cliente)
admin.site.register(Vivienda)
admin.site.register(Actividad)