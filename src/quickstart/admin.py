from django.contrib import admin
from .models import Article, Genre, Movie, User
from user.models import User

admin.site.register(Article)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(User)

