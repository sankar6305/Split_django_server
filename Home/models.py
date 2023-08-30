from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Snippets(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
    