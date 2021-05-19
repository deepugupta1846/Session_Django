from django import forms
from .models import *


class signup(forms.ModelForm):
    class Meta:
        model = SignupData
        fields = ['Name', 'Mob_No', 'Email','Gender', 'Password']
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class': 'form-control'}),
            'Mob_No': forms.TextInput(attrs={'placeholder': 'Enter Mob no', 'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Password': forms.TextInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'})
        }


class updateform(forms.ModelForm):
    class Meta:
        model = SignupData
        fields = ['Name', 'Mob_No', 'Gender', 'Email']
        widgets = {
            'Name' : forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class': 'form-control'}),
            'Mob_No': forms.TextInput(attrs={'placeholder': 'Enter Mob no', 'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),

        }



