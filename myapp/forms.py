from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'body']

def Contactdata(request):
    f = ContactForm(request.POST)
    f.is_valid()
    f.save()