from django import forms
from .models import contacts

class FormSubmitForm(forms.ModelForm):
    
    class Meta:
        
        model = contacts
        fields = '__all__'