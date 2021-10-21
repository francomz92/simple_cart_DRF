from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
   list_display = ['id', 'username', 'email', 'image', 'is_active', 'is_staff', 'is_superuser']
   list_display_links = ['id', 'username']
   ordering = ['id']
   search_fields = ['id', 'username', 'email']
   fieldsets = [
       (_('Personal data'), {
           'fields': ['first_name', 'last_name', 'image']
       }),
       (_('Credentials'), {
           'fields': ['username', 'email', 'password', 'last_login']
       }),
       (_('Status'), {
           'fields': [('is_active', 'is_staff', 'is_superuser')]
       }),
       (_('Permissions'), {
           'classes': ['collapse'],
           'fields': ['user_permissions', 'groups']
       }),
   ]