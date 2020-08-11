from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, FileInput, Select, NumberInput

from house.models import House


class UserRentHouseForm(ModelForm):
    class Meta:
        model = House
        fields = ('category','title', 'keywords','description','image','address','price','room','balcony',
                  'heating','stuff','detail','slug',)
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),

            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'room': Select(attrs={'class': 'form-control', 'placeholder': 'Room'}),
            'balcony': Select(attrs={'class': 'form-control', 'placeholder': 'balcony'}),
            'heating': Select(attrs={'class': 'form-control', 'placeholder': 'heating'}),
            'stuff': Select(attrs={'class': 'form-control', 'placeholder': 'stuff'}),
            'detail': CKEditorWidget(),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),

        }
