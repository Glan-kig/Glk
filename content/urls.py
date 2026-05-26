from django.urls import path, include
from rest_framework import routers
from content.views import PostViewSet, CategoryViewSet, ArticleViewSet, RegisterView, LoginView, TagViewSet, MediaViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'tags', TagViewSet)
router.register(r'media', MediaViewSet)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
]