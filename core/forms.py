from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ny anarana fampiasanao',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))   
     
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Avereno eto le teny miafina',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ny teny miafina tinao ho ampiasaina',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Ny adressy mailaka fampiasanao',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ny anarana fampiasanao',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))   
     
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Avereno eto le teny miafina',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #121417;'
    }))
    