from django.db import models


# Create your models here.
class Menu(models.Model):
    """
    Defines the Menu params
    """
    uuid = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    published_date = models.DateTimeField(max_length=10, unique=True,)
    update_date = models.DateTimeField(auto_now=True)
