from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


# Create your models here.


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

    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    search_word = models.CharField(max_length=200)
    filter = models.CharField(max_length=100, choices=Order, default=DATE)
    search_date = models.DateTimeField(default=timezone.now)

    def format(self):
        return f'{str(self.transaction_id)}, {str(self.user)},  {str(self.search_word)}, {str(self.search_date)}'

    def __str__(self):
        return self.format()


class Function(models.Model):
    """
    Table contains information about available function (
    """
    Admin = 'Admin'
    Moderator = 'Moderator'

    Functions = [
        (Admin, 'Admin'),
        (Moderator, 'Moderator'),
    ]

    permission_id = models.AutoField(primary_key=True)
    function = models.CharField(max_length=100, choices=Functions)
    user = models.ManyToManyField(User)

    def format(self):
        return f'{self.permission_id}, {self.function}'

    def __str__(self):
        return self.format()


class Rating(models.Model):
    """
    Table contains information about review and rates for page
    """
    review = models.CharField(max_length=200, blank=True)
    rate = models.PositiveSmallIntegerField(default=5, validators=[MaxValueValidator(5)])
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def format(self):
        return f'{str(self.review)}, {str(self.rate)}, {(str(self.author))}, self{str(self.date)}'

    def __str__(self):
        return self.format()


class Favourites(models.Model):
    """ Model contains info about user and favorites moviews"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.CharField(max_length=200)

    def format(self):
        return f'{str(self.owner)}, {str(self.favorites)}'

    def __str__ (self):
        return self.format()


