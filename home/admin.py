from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile, FAQ


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', 'note']
    readonly_fields = ('status',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'image_tag', 'phone', 'city', 'country']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['ordernumber','question', 'answer', 'status']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FAQ, FAQAdmin)
