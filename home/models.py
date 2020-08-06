from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea

# Create your models here.
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    smtpserver = models.CharField(max_length=50, blank=True)
    smtpemail = models.CharField(max_length=50, blank=True)
    smtppassword = models.CharField(max_length=50, blank=True)
    smtpport = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': '5'}),
        }


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    adress = models.CharField(blank=True, max_length=120)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + ']'

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'adress', 'city', 'country', 'image']
