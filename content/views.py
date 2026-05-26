from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Post, Category, CustomUser, Article
from .serializers import PostSerializer, CategorySerializer, UserSerializer, ArticleSerializer
from .permissions import IsAdminOrEditor
from django.contrib.auth import authenticate

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes: list = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes: list = [permissions.AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        username: str = request.data.get('username')
        password: str = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            return Response({"message": "Login successful", "user": UserSerializer(user).data})
        return Response({"message": "Invalid credentials"}, status=400)
    
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes: list = [permissions.IsAuthenticated, IsAdminOrEditor]

    def create(self, request: Request, *args, **kwargs) -> Response:
        return super().create(request, *args, **kwargs)
    
    def update(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)