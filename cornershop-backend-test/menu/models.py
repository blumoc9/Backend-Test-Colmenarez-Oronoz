from django.db import models
from uuid import uuid4


# Create your models here.
class Menu(models.Model):
    """
    Defines the Menu params
    """
    uuid = models.CharField(max_length=50, null=False, unique=True, blank=False, default="")
    name = models.CharField(max_length=50, default="")
    published_date = models.CharField(max_length=10, default="", unique=True)
    update_date = models.TextField()
