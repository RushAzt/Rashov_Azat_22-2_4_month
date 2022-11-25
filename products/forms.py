from django import forms
from .models import Product


class ProductCreateForm(forms.Form):
    title = forms.CharField(min_length=10, max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField(widget=forms.NumberInput)
    amount = forms.IntegerField(widget=forms.NumberInput)

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=8, max_length=150)