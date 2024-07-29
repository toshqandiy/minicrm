from django import forms

from .models import *

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'phone_number', 'address')