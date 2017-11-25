from TaxApp.models import Product,Code,Result,Taxation
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea


class ProductForm(forms.ModelForm):
     product_name=forms.CharField( widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),)
     quantity=forms.IntegerField( widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),)
     cost_price=forms.FloatField( widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),)
     selling_price=forms.FloatField( widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),)
   
     class Meta: 
        model = Product
        fields = ('product_name', 'quantity', 'cost_price','selling_price','category')
        labels = {
                'product_name': ('Product Name'),
                'quantity':('Quantity'),
                'cost_price': ('Cost price'),
                'selling_price':('Selling Price'),
                'category':('Category'),
                }


