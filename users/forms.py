from ast import Assert
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from dashboard.views import add_asset


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class AssetForm(forms.ModelForm):
    class Meta:
        model = add_asset
        fields = ['name', 'category', 'assigned_to', 'cost']