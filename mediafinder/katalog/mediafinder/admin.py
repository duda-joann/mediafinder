from django.contrib import admin
from .models import Search, Rating, Function

# Register your models here.

admin.site.register(Search),
admin.site.register(Rating),
admin.site.register(Function)

