from django import forms
from .models import Product

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adı', 'required': True}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Şifre', 'required': True}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['english_product_name', 'french_product_name', 'english_product_color', 'french_product_color', 'product_image']