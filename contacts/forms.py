from django import forms
from .models import Contact
from django.forms import ModelForm, RadioSelect

class ContactForm(ModelForm):    
    class Meta:
        model = Contact 
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'role': RadioSelect(choices=['regular', 'admin'],),
        }