from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name: str = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name: str = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('author', 'Author'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='author')

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"
    
class Post(models.Model):
    title: str = models.CharField(max_length=200)
    content: str = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    title: str = models.CharField(max_length=200)
    content: str = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='articles')
    tags = models.ManyToManyField(Tag, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class Media(models.Model):
    file: str = models.FileField(upload_to='media/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Media {self.id} uploaded by {self.uploaded_by.username}"