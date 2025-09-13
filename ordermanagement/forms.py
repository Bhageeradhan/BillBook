#from django.forms import ModelForm
from django import forms
from .models import *

class Customer_Form(forms.ModelForm):
    
    class Meta:
        
        model = Customers
        fields = '__all__'
        widgets = {
            'customer_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Name:'}),
            'customer_since':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Since:'}),
        }
        
class Orders_Form(forms.ModelForm):
    
    class Meta:
        
        model = order
        fields = ['customer_ref','product_ref','order_number','order_date','quantity']
        
        widgets = {
            'customer_ref':forms.Select(attrs={'class':'form-control'}),
            'product_ref':forms.Select(attrs={'class':'form-control'}),
            'order_number':forms.TextInput(attrs={'class':'form-control'}),
            'order_date':forms.DateInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'gst_amount':forms.NumberInput(attrs={'class':'form-control'}),
            'bill_amount':forms.NumberInput(attrs={'class':'form-control'})
        }
    