from django.db import models

# Create your models here.
from menu.models import Menu


class Option(models.Model):
    """Defines the MenuDetail data fields"""
    code = models.CharField(max_length=50, default="")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="options")
    description = models.CharField(max_length=250, default="")
    is_vegan = models.BooleanField(default=False)
    chef_comments = models.CharField(max_length=250, default=""),
    publish_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ['option']
        ordering = ['-publish_date']
        verbose_name_plural = 'options'

    def __str__(self):
        return '{}'.format(self.description)
