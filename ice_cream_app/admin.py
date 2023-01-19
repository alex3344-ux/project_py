from django.contrib import admin

# Register your models here.

from .models import Ice_cream, Market

admin.site.register(Ice_cream)
admin.site.register(Market)

