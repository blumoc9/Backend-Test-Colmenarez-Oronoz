from django import forms
from .models import Option


class OptionMenuForm(forms.ModelForm):
    """Defines the MenuDetail data fields"""

    class Meta:
        model = Option
        fields = ('description', 'is_vegan')

