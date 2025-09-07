# models.py
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    creado = models.DateTimeField(default=timezone.now)
    # SOLO AGREGAR ESTA LÍNEA:
    max_comentarios = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.titulo
    
    # SOLO AGREGAR ESTOS 2 MÉTODOS:
    def total_comentarios(self):
        return self.comentarios.count()
    
    def puede_comentar(self):
        return self.total_comentarios() < self.max_comentarios


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$',
                message="El nombre solo puede contener letras y espacios"
            )
        ]
    )
    contenido = models.TextField(max_length=300)  # limita a 300 caracteres
    creado = models.DateTimeField(default=timezone.now)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        return f"{self.autor} - {self.post.titulo}"
