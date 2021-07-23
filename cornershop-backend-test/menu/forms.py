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



