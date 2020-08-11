from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=30, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
    slug = models.SlugField(null=False, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'slug': self.slug})


class Images(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)

    image_tag.short_description = 'Image'
