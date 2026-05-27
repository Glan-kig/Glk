from rest_framework import serializers
from .models import Post, Category, CustomUser, Article, Tag, Media, Notification

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields: list[str] = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields: list[str] = ['id', 'name']
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields: list[str] = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list[str] = ["id", "username", "email", "role"]

class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields: list[str] = ["id", "title", "content", "author", "status", "categories", "tags", "created_at", "updated_at"]

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields: list[str] = ["id", "file", "uploaded_by", "created_at"]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields: list[str] = ["id", "recipient", "message", "is_read", "created_at"]