from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from main.managers import UserSearchManager


class Search(models.Model):
    """
    table  contains information
    about signed in user and search word.
    Params: value used to order results
    """

    DATE = 'date'
    RATING = 'rating'
    TITLE = 'title'
    VIEWS = 'viewcount'

    Order = [
        (DATE, 'Date'),
        (RATING, 'Rating'),
        (TITLE, 'Title'),
        (VIEWS, 'Views'),
    ]

    transaction_id = models.AutoField(primary_key=True,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    search_word = models.CharField(max_length=200)
    result_url = models.CharField(max_length = 200)
    filter = models.CharField(max_length=100, choices=Order, default=DATE)
    search_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()
    search_by_user = UserSearchManager()
    objects = models.Manager()

    def format(self):
        return f'{str(self.transaction_id)}, {str(self.user)},  {str(self.search_word)}, {str(self.search_date)}'

    def __str__(self):
        return self.format()

    def save(self, *args, **kwargs):
        slug_str = f'{str(self.result_url)}'
        self.slug = slug_str
        super(Search, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("app:view", kwargs={'slug': self.slug})
