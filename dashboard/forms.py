from django import forms
from .models import Asset, Order # type: ignore

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['asset', 'status']
