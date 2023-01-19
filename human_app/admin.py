from django.contrib import admin

# Register your models here.


from django.contrib import admin

# Register your models here.

from .models import Human, Children, PersonRelationShip

admin.site.register(Human)
admin.site.register(Children)
admin.site.register(PersonRelationShip)

