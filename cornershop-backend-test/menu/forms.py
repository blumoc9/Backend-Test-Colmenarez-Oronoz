from django import forms

from menu.models import Menu

"""
Create form only parameter date, because when save the objectMenu 
will generate uuid  with uuid4
"""


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'published_date']


class MenuDetailForm(forms.Form):
    """
    Defines MenuDetail fields
    """
    description = forms.CharField(max_length=250, required=True)
    is_vegan = forms.BooleanField(required=False)
    chef_comments = forms.CharField(max_length=250, required=False)


class OrderForm(forms.Form):
    """
    Defines Order fields
    """
    name = forms.CharField(max_length=250)
    customization = forms.CharField(max_length=250)
