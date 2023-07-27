from django.db import models

# Create your models here.

class Award(models.Model):
    description = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='Award/',blank=True)