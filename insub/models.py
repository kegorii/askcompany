from django.db import models

class Insub(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    introduce = models.TextField()
