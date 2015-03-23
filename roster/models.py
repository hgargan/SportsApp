from django.db import models

class Player(models.Model):
    name = models.CharField(unique=False, max_length=50)