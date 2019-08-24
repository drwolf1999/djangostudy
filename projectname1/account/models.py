from django.db import models

# Create your models here.

class Account(models.Model):
    userId = models.CharField(primary_key=True, unique=True, max_length=15)
    password = models.CharField(max_length=15)
    nick = models.CharField(max_length=10)