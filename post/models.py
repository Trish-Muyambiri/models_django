from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=5000)
