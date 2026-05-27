from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from .models import Post, Category, CustomUser, Article, Tag, Media, Notification
from .serializers import PostSerializer, CategorySerializer, UserSerializer, ArticleSerializer, TagSerializer, MediaSerializer, NotificationSerializer
from .permissions import IsAdminOrEditor, CanPublishArticle, CanCreateDraft
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes: list = [permissions.IsAuthenticated, IsAdminOrEditor]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes: list = [permissions.IsAuthenticated, IsAdminOrEditor]

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
    
    def get_permissions(self) -> list:
        if self.action in ['create', 'update']:
            return [CanCreateDraft()]
        elif self.action == 'publish':
            return [CanPublishArticle()]
        return [permissions.IsAuthenticated()]

    def create(self, request: Request, *args, **kwargs) -> Response:
        return super().create(request, *args, **kwargs)
    
    def update(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)
    
    def perform_create(self, serializer) -> None:
        article = serializer.save()

        editors = User.objects.filter(role__in=['admin', 'editor'])
        for editor in editors:
            Notification.objects.create(
                recipient=editor, 
                message=f"Nouvel article en attente : '{article.title}' créé par {article.author.username}"
            )

    @action(detail=True, methods=['post'])
    def publish(self, request: Request, pk=None) -> Response:
        article = self.get_object()
        article.status = 'published'
        article.save()
        return Response({"message": "Article published", "status": article.status})
    
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes: list = [permissions.IsAuthenticated, IsAdminOrEditor]

    def create(self, request: Request, *args, **kwargs) -> Response:
        return super().create(request, *args, **kwargs)
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes: list = [permissions.IsAuthenticated]