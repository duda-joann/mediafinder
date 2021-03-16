from django.db import models
from django.contrib.auth.models import UserManager, User
from django.conf import settings
from .validator import validate_age
# Create your models here.



class CustomUserManager(UserManager):
    pass


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True, null=True)
    #email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField(validators=[validate_age])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email, self.date_of_birth

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
