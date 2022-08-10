from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
