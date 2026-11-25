from django import forms 
from .models import Products, ProductSpec


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "title",
            "price",
            "quantity",
            "description",
            "category",
            "status",
            "thumbnail"
        ]