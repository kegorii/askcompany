from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    pcreated_at = models.DateTimeField(auto_now=True)
    