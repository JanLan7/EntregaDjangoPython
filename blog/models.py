from django.db import models
from django.utils import timezone

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre")
    subtitle = models.CharField(max_length=150, verbose_name="Autor")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='pages/', blank=True, null=True, verbose_name="Imagen")
    genre = models.CharField(max_length=50, verbose_name="Género", default="Ficción")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Calificación", default=4.0)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

    def __str__(self):
        return self.title
