from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'get_html_avatar']
    list_display_links = ['username']
    search_fields = ['username', 'first_name']
    readonly_fields = ('get_html_avatar', )

    def get_html_avatar(self, object):
        if object.avatar:
            return mark_safe(f'<img src="{object.avatar.url}", width="50">')

    get_html_avatar.short_description = 'Аватар'


admin.site.register(UserProfile, UserProfileAdmin)
