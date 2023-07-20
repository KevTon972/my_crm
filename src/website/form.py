from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    password1 = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'password'}))
    password2 = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'confirmation password'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email adress'}))


    class Meta:
        model=User
        fields = ('username', 'password1', 'password2', 'email')