from django.db import models

class Hero(models.Model):
    name = models.TextField(default='')

