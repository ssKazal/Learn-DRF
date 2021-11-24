from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'article', views.ArticleViewSet, basename='article')
router.register(r'author', views.AuthorViewSet, basename='author')
router.register(r'genres', views.GenreViewSet, basename='genre')
router.register(r'movies', views.MovieViewSet, basename='movie')


urlpatterns = [
    path('api/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', views.article, name='article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]
