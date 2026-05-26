from django.urls import path, include
from rest_framework import routers
from content.views import PostViewSet, CategoryViewSet, ArticleViewSet, RegisterView, LoginView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]