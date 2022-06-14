from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=500)
    # charfield vs textfield?
