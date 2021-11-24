from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Article, Movie, Genre, User


# ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})
    confirm_password = serializers.CharField(write_only = True, style = {'input_type': 'password'})

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'confirm_password', 'groups', 'articles']

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if not password or not confirm_password:
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if password != confirm_password:
            raise serializers.ValidationError("Those passwords don't match.")
        else:
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Serializer
"""
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
"""

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['genre'] = GenreSerializer(instance.genre).data
        return response