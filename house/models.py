from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=30, choices=STATUS)
    slug = models.SlugField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class House(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    BALCONY = (
        ('Existent', 'Var'),
        ('Absent', 'Yok'),
    )
    HEATING = (
        ('Yok', 'Yok'),
        ('Soba', 'Soba'),
        ('Kombi', 'Kombi'),
        ('Merkezi', 'Merkezi'),
    )
    STUFF = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    ROOM = (
        ('1+0', '1+0'),
        ('1+1', '1+1'),
        ('2+0', '2+0'),
        ('2+1', '2+1'),
        ('3+1', '3+1'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    address = models.TextField()
    price = models.IntegerField(blank=True)
    room = models.CharField(max_length=30, choices=ROOM, blank=True)
    balcony = models.CharField(max_length=30, choices=BALCONY, blank=True)
    heating = models.CharField(max_length=30, choices=HEATING, blank=True)
    stuff = models.CharField(max_length=30, choices=STUFF, blank=True)
    status = models.CharField(max_length=30, choices=STATUS)
    detail = RichTextUploadingField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
