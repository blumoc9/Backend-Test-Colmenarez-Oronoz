from django import forms

from menu.models import Menu


class OptionMenuForm(forms.ModelForm):
    """
    Defines MenuDetail fields
    """
    class Meta:
        model = Menu
        fields = ['name', 'published_date']
