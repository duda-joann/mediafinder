from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Rating(models.Model):
    """
    Table contains information about review and rates for page
    """
    review = models.CharField(max_length=200, blank=True)
    rate = models.PositiveSmallIntegerField(default=5, validators=[MaxValueValidator(5)])
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)

    def format(self):
        return f'{str(self.review)}, {str(self.rate)}, {(str(self.author))}, self{str(self.date)}'

    def __str__(self):
        return self.format()
