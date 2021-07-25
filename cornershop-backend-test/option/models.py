from django.db import models

# Create your models here.
from menu.models import Menu


class Option(models.Model):
    """Defines the MenuDetail data fields"""
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="options")
    menu_uuid = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, default="")
    is_vegan = models.BooleanField(default=False)
    publish_date = models.CharField(max_length=10, default="")
    update_date = models.CharField(max_length=10, default="")
