from django.db import models
from django.utils import timezone
from django.conf import settings

from .search import Search


class Favourites(models.Model):
    """ Model contains info about user and favorites moviews"""
    transaction_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_url = models.ManyToManyField(Search)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.owner, self.video_url, self.creation_date
