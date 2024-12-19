from django.db import models

# Create your models here.
from django.db import models
# Modelo para Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Tarea
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Modelo para Nota
class Nota(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota para: {self.tarea.titulo}"