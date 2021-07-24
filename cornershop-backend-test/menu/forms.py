import datetime

from django import forms
from datetime import datetime

"""
Create form only parameter date, because when save the objectMenu 
will generate uuid  with uuid4
"""


class MenuForm(forms.Form):
    name = forms.CharField(max_length=50)
    publish_date_input = forms.CharField()
