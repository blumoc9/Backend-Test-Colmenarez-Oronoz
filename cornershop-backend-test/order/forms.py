from django import forms

from order.models import Order


class OrderMenuForm(forms.ModelForm):
    """Defines the Order data fields"""

    class Meta:
        model = Order
        fields = ('customization', 'phone_number')
        labels = {
            'customization': 'customizations(e.g no tomatoes in salad)',
            'phone_number': 'cellphone (eg: 569xxxxxx99)'
        }
