from django.contrib import admin

# Register your models here.
from house.models import Category, House, Images


class HouseImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'price', 'room']
    list_filter = ['status']
    inlines = [HouseImageInline]
    readonly_fields = ('image_tag',)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'house', 'image_tag']  # buradaki title image ler home modeldeki ile aynı olmalı
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Images, ImagesAdmin)
