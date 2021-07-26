from django.db import models

from option.models import Option


class Order(models.Model):
    """
    Defines the Order data fields
    """
    option = models.ForeignKey(Option, on_delete=models.PROTECT)
    order_uuid = models.CharField(max_length=50, default="")
    option_uuid = models.CharField(max_length=50, default="")
    customization = models.CharField(max_length=250, default="",)
    username = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=50, default="")
    status_order = models.BooleanField(default=False)

    def __str__(self):
        return self.order_uuid
