from django.contrib import admin

# Register your models here.
from .models import Brands,Mobile

admin.site.register(Brands)
admin.site.register(Mobile)
