from django.db import models
from django.utils import timezone

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
