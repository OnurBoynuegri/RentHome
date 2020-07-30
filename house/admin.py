from django.contrib import admin

# Register your models here.
from house.models import Category, House, Images

class HouseImageInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'room']
    list_filter = ['status']
    inlines = [HouseImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'house', 'image']#buradaki title image ler home modeldeki ile aynı olmalı


admin.site.register(Category, CategoryAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Images, ImagesAdmin)
