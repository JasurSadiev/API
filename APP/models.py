from django.db import models

# Create your models here.
class Newton(models.Model):
    title = models.CharField(max_length = 300)
    body = models.TextField()
