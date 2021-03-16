from django.db import models


class SearchQuerySet(models.QuerySet):
    def users(self):
        return self.filter(user=self.request.user)


class SearchManager(models.Manager):
    pass


UserSearchManager = SearchManager.from_queryset(SearchQuerySet)