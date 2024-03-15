from django import forms

from .models import MyUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username','first_name','last_name','email', 'phone','city','date_of_brith','country','profile_pic','password',]
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_brith': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'profile_pic' : forms.FileInput(attrs={'class':'form-control'}),
        }
    
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())