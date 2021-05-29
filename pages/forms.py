from django import forms
from pages.models import *


class ProductForm(forms.Form):
    code = forms.CharField(max_length=300)
    description = forms.CharField(max_length=300)
    ean = forms.IntegerField(default=None)
    url = forms.URLField(default="")
    image_url = forms.URLField(default="")
    company = forms.ModelChoiceField(queryset=Company.objects.all())
