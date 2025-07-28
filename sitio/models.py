from django.db import models

class Biografia(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='biografia/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Destacado(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='destacados/')
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo
