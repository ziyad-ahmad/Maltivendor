from django import forms
from .models import Products, Order 

class OrederForm (forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'city','address','email','posta_code')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('category', 'name', 'description', 'image', 'initial_sell', 'color', 'brand', 'status', 'domain_user')
        widgets = {
            'category': forms.Select(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300"
            }),
            'name': forms.TextInput(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
                "placeholder": "Product Name"
            }),
            'description': forms.Textarea(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
                "rows": 4,
                "placeholder": "Product Description"
            }),
            'image': forms.FileInput(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
            }),
            'initial_sell': forms.NumberInput(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
                "placeholder": "Selling Price"
            }),
            'color': forms.TextInput(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
                "placeholder": "Color"
            }),
            'brand': forms.TextInput(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300",
                "placeholder": "Brand"
            }),
            'status': forms.Select(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300"
            }),
            'domain_user': forms.Select(attrs={
                "class": "p-2 m-2 border border-gray-300 rounded-lg bg-white text-gray-700 focus:ring focus:ring-indigo-500 transition duration-300"
            }),
        }