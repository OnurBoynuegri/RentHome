from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }


CITY = {
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),

}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', "adress", 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': Select(attrs={'class': 'form-control', 'placeholder': 'Şehir'}, choices=CITY),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
        }
