from django.contrib import admin

# Register your models here.

from .models import MenuItem, Menu

admin.site.register(MenuItem)
admin.site.register(Menu)