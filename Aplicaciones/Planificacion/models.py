from django.db import models

# Create your models here.
class Constructora(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def str(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def str(self):
        return self.nombre

class Vivienda(models.Model):
    direccion = models.TextField()
    tipo = models.CharField(max_length=100)  # Ejemplo: "Casa", "Departamento"
    metros_cuadrados = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=[("En construcción", "En construcción"), ("Terminada", "Terminada")])
    

    def str(self):
        return f"{self.tipo} - {self.direccion}"

class Actividad(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[("Pendiente", "Pendiente"), ("En progreso", "En progreso"), ("Finalizada", "Finalizada")])
    foto = models.ImageField(upload_to='actividades', null=True, blank=True, verbose_name="Foto Adjunta")
    email = models.EmailField(null=True, blank=True)
        
    def str(self):
        return f"{self.descripcion} - {self.estado}"