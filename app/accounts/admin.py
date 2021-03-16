from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    model = CustomUser
    list_display = ['name']
    list_filter = ['date_of_birth']
    filter_horizontal = []
    ordering = ['is_staff']



admin.site.register(CustomUser, CustomUserAdmin)
