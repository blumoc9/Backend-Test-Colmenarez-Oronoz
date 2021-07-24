from django.db import models
import datetime


# Create your models here.
class Menu(models.Model):
    """
    Defines the Menu params
    """
    uuid = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    published_date = models.CharField(max_length=50, default="", unique=True)
    update_date = models.TextField()
