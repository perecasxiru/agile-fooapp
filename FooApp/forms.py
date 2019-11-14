from django import forms
from django.contrib.auth.models import User

from FooApp.models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User: test, Pass: 1234'}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']