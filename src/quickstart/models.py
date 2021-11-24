from django.db import models
from user.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        User, related_name='articles', on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.SET_NULL, null=True)
    number_in_stock = models.PositiveIntegerField()
    daily_rental_rate = models.FloatField()

    def __str__(self):
        return self.title
