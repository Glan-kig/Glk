from rest_framework import serializers
from .models import Post, Category, CustomUser, Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields: list[str] = '__all__'
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields: list[str] = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list[str] = ["id", "username", "email", "role"]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields: list[str] = ["id", "title", "content", "author", "created_at", "updated_at"]