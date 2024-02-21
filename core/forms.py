from django.forms import ModelForm
from django import forms
from core.models import ContactMail

class ContactForm(ModelForm):
    
    class Meta:
        model = ContactMail
        fields = ['email', 'message']
        
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Your Email Address', 'class':'stext-111 cl2 plh3 size-116 p-l-62 p-r-30'}),
            'message': forms.Textarea(attrs={'placeholder':'How Can We Help?', 'class':'stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25'})
        }