from django import forms


class OrderForm(forms.Form):
    """
    Defines Order fields
    """
    name = forms.CharField(max_length=250)
    customization = forms.CharField(max_length=250)
