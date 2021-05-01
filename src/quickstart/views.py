from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from django.views.decorators.csrf import csrf_exempt

from .permissions import IsSuperuser, IsCourseAdmin
from .serializers import UserSerializer, GroupSerializer, ArticleSerializer
from .models import Article


############# quick tutirial ########################
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


############# Fuction based api view ##################
"""
@csrf_exempt
def article(request):
    # list of article
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    # create article
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # retrive data
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    # update the retrive data
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    # delete the retrive data
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
"""


############# Fuction based api view with decorator @api_view ##################
@api_view(['GET', 'POST'])
def article(request):
    # list of article
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    # create article
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # retrive data
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # update the retrive data
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete the retrive data
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################ viewset #####################################
"""
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


############## modelviewset, DjangoFilterBackend ################
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsSuperuser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


############## modelviewset, SearchFilter ################
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticated, IsSuperuser]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title']


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author='Kazal')
