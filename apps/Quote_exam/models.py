from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UserManager(models.Manager):
#     def login(self, postData):

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

class Quote(models.Model):
    author = models.CharField(max_length = 50)
    quotes = models.CharField(max_length = 500)
    user = models.ForeignKey(User, related_name = 'quote')

class Favorites (models.Model):
    authfavorite = models.CharField(max_length = 100)
    quotefavorite = models.CharField(max_length = 100)
    quote = models.ForeignKey(Quote, related_name = 'QuoteFavorites')
    userfavorites = models.ForeignKey(User, related_name = 'UserFavorites')
    # objects = UserManager()
